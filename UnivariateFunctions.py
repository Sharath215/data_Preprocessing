class Univariate():
    

    
    def quanQual(dataset):
        
        quan = []
        qual = []
        for columnName in dataset.columns:
            if(dataset[columnName].dtype == 'O'):
                qual.append(columnName)
            else:
                quan.append(columnName)
                
        return quan,qual
        
    def Frequency_Table(C_Name,dataset):
        
        import numpy as np
        import pandas as pd
        
        Freq_Table = pd.DataFrame(columns = ["Unique_Values","Frequency","Relative_Frequency","CumSum"])
        Freq_Table["Unique_Values"] = dataset[C_Name].value_counts().index
        Freq_Table["Frequency"] = dataset[C_Name].value_counts().values
        Freq_Table["Relative_Frequency"] = (Freq_Table["Frequency"]/103)
        Freq_Table["CumSum"] = Freq_Table["Relative_Frequency"].cumsum()
        return Freq_Table    
    
    def Central_Tendency(Quan,dataset):
        
        import numpy as np
        import pandas as pd
        
        Descriptive = pd.DataFrame(index=["Mean","Median","Mode"], columns = Quan) 
        for name in Quan: 
            Descriptive[name]['Mean']    = dataset[name].mean()
            Descriptive[name]['Median']  = dataset[name].median()
            Descriptive[name]['Mode']    = dataset[name].mode()[0]
        return Descriptive
    
    def Percentile(Quan,dataset):
        
        import numpy as np
        import pandas as pd
        
        Descriptive = pd.DataFrame(index=["Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%"], columns = Quan) 
        for name in Quan: 
            Descriptive[name]['Q1:25%']   = dataset.describe()[name]['25%']
            Descriptive[name]['Q2:50%']   = dataset.describe()[name]['50%']
            Descriptive[name]['Q3:75%']   = dataset.describe()[name]['75%']
            Descriptive[name]['99%']      = np.percentile(dataset[name],99)
            Descriptive[name]['Q4:100%']  = dataset.describe()[name]['max']
        return Descriptive
    
    def IQR(Quan,dataset):
        
        import numpy as np
        import pandas as pd
        
        Descriptive = pd.DataFrame(index=["IQR", "1.5Rule", "Lesser", "Greater", "Min", "Max"], columns = Quan)
        for name in Quan: 
            Descriptive[name]['Q4:100%']  = dataset.describe()[name]['max']
            Descriptive[name]['IQR']      = dataset.describe()[name]['75%'] - dataset.describe()[name]['25%']
            Descriptive[name]['1.5Rule']  = 1.5 * Descriptive[name]['IQR']
            Descriptive[name]['Lesser']   = dataset.describe()[name]['25%'] - Descriptive[name]['1.5Rule']
            Descriptive[name]['Greater']  = dataset.describe()[name]['75%'] + Descriptive[name]['1.5Rule']
            Descriptive[name]['Min']      = dataset[name].min()
            Descriptive[name]['Max']      = dataset[name].max()
            
        return Descriptive
    
    def get_Outliers_list(Descriptive,quan):
        
        lesser=[]
        greater=[]
        
        for Name in quan:
            if (Descriptive[Name]['Lesser']>Descriptive[Name]['Min']):
                lesser.append(Name)
            if (Descriptive[Name]['Greater']<Descriptive[Name]['Max']):
                greater.append(Name)
                
        return lesser,greater
    
    def Outliers_Replace(lesser,greater,dataset,Descriptive):
        for N in lesser:
            dataset[N][dataset[N]<Descriptive[N]['Lesser']] = Descriptive[N]["Lesser"]

        for N in greater:
            dataset[N][dataset[N]>Descriptive[N]['Greater']] = Descriptive[N]["Greater"]
            
        return dataset

    def HSK(Quan,dataset):
        
        import numpy as np
        import pandas as pd
        
        Descriptive = pd.DataFrame(index=["Skew", "Krutosis"], columns = Quan)
        
        for name in Quan:
            
            Descriptive[name]['Skew']      = dataset[name].skew()
            Descriptive[name]['Krutosis']      = dataset[name].kurtosis()
            
        return Descriptive
        