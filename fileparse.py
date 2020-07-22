import csv

def parse_csv(filename, select=None, types=None, has_headers = True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        
        # Read the file headers
        if has_headers:
            headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices]
            
            if types:
                row = [func(val) for func, val in zip(types, row)]

            
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records

records= parse_csv('Data/portfolio.csv', types= [str, int, float])
print(records)
records= parse_csv('Data/portfolio.csv', types= [str, int], select = ['name', 'shares'])
print(records)
records= parse_csv('Data/prices.csv',types = [str, float], has_headers=False)
print(records)

records= parse_csv('Data/portfolio.dat',types = [str,int, float], delimiter= ' ')
print(records)