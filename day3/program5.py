def intersection(lt1, lt2): 
    return list(set(lt1) & set(lt2)) 
  
lt1 = input("Enter first list=") 
lt2 = input("Enter second list=")
print(intersection(lt1,lt2)) 
