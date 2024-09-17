


def alter(curser):
    table_name=input("Table name u want to alter:")
    column_name=input("column u want to add:")
    n=f"""alter table {table_name}
        add {column_name} varchar(25)"""
    curser.execute(n,column_name)
    return "successfully"


def truncate(curser):
    table_name=input("Table name u want to Truncate:")
    l=f"""truncate table {table_name}"""
    curser.execute(l)
    return "successfully"
 
def On_where_condition(curser):
    table_name=input("table_name u want to display:")
    column_name=input("column name u want to retrive:")
    value=input("value of that column value")
    k=f"""select * from {table_name}
    where {column_name}=?"""
    curser.execute(k,value)
    l=curser.fetchall()
    j=[]
    for i in l:
        j.append(i)
    return j
 

 

 
 
 