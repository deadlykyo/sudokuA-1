import csv

class CSVImport:

    def get_rows_sudoku_data(self,file_sudoku,delimeter):
        """
        Read the sudoku data form a csv file
        Returns a matrix[][] which contain all the sudoku
        data into the csv file and their size

        Keyword arguments:
        sudoku_file -- the path of the file which contains the
                       sudoku data
        delimeter -- the separator for data in the csv file               

        """
        
        res = []
        try:
            with open(file_sudoku, 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=delimeter, quotechar='|')
                for row in spamreader:
                    res.append(row)
            res = self.get_sudoku_raws_data_from_csv_rows(res)
        except Exception:
            res = []
        return res

    def get_sudoku_raws_data_from_csv_rows(self,csv_rows):
        """
        Given the rows form the csv file it converts the
        each row in a valid row entry for the sudoku solver
        Returns a matrix[][] which contain the sudoku data
        in each row and their size of the sudoku

        Keyword arguments:
        csv_rows -- the rows into a csv file         
        """
        
        res = []
        for row in csv_rows:
            self.get_sudoku_raw_data(row)
            res.append(self.get_sudoku_raw_data(row))
        return res
        

    def get_sudoku_raw_data(self,csv_sudoku):
        """
        Given a row form the csv file it converts the row
        in a valid row entry for the sudoku solver
        Returns an array[] which contain the sudoku data
        in the row and the size of the sudoku

        Keyword arguments:
        csv_sudoku -- A row of the csv file         
        """
        res = ""
        size = -1
        for data in csv_sudoku:
            res = res + data+"\n"
            if size == -1:
                size = len(data)
            elif size != len(data):
                size = -1
                break
        if len(csv_sudoku) != size:
            size = -1
        return res,size
        
