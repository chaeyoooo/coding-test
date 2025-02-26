# def solution(data, ext, val_ext, sort_by):
#     newext = { "code" : 0 , "date" : 1, "maximum" : 2 , "remain" : 3}
#     newsort = { "code" : 0 , "date" : 1, "maximum" : 2 , "remain" : 3}
#     for i in data:
#         a = newext.get(ext)
#         if i[a] >= val_ext:
#             del i
#             b = newsort.get(sort_by)
#             data.sort(key == b)
#     return data
            
def solution(data, ext, val_ext, sort_by):
    newext = { "code": 0, "date": 1, "maximum": 2, "remain": 3 }
    newsort = { "code": 0, "date": 1, "maximum": 2, "remain": 3 }
    
    for i in data[:]:  
        a = newext.get(ext)
        if i[a] >= val_ext:
            data.remove(i) 
        
    b = newsort.get(sort_by)
    data.sort(key=lambda x: x[b])  

    return data

            
            
        