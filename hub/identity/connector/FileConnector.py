#hub imports
from identity.interface.BasicConnector import BasicConnector

#python lib imports
import os.path


class DelimitedFileConnector( BasicConnector ):

    #boolean defining what connector supports
    supports_import_accounts_full = True
    supports_import_accounts_delta = False
    supports_import_accounts_single = False

    #configuration for processing the file
    filename = "/home/briancap/Documents/hub_users.csv"
    has_header_row = True
    delimiter = ","

    #positions for each field

    connection = None
    
    def getConnection( self ):
        print( 'STARTING getConnection' )
    
        if os.path.isfile( self.filename ):
            return open( self.filename )
        
        print( 'ENDING getConnection' )


    def importAccountsFull( self ):
        print( 'STARTING importAccounts' )

        fileContents = self.getFileContents()
        
        print( 'ENDING importAccounts' )



    def importUsersFull( self ):
        print( 'STARTING importUsersFull' )

        fileContents = self.getFileContents()

        print( 'ENDING importUsersFull' )



    def getFileContents( self ):
        print( 'STARTING getFileContents' )

        allFileContents = list()

        if( self.connection is None ):
            self.connection = self.getConnection()
        
        rowCount = 0

        print( 'afer rowCout var defined' )

        #loop populates allFileContents with sanitized field values
        for line in self.connection:
            print( 'Looping over line: ' + str(rowCount) )        
            #loop over every row in the file, first row will be skipped if it is a header
            if( ( self.has_header_row and rowCount > 0 ) or not self.has_header_row ):

                #single rows are split based off the global delimiter
                rowArray = line.split( self.delimiter )
                
                #0 based field counter that tracks position of a field in rowArray
                fieldCount = 0

                for field in rowArray :
                    #loop over individual fields in a line, rstrip removes \n characters
                    # there is always a \n in the last field of every row
                    sanitizedField = field.rstrip()
                    rowArray[ fieldCount ] = sanitizedField
                    fieldCount += 1
                
                #add sanitized row to fieldContents array
                allFileContents.append( rowArray )

            #increment count for adding rows positionally to allFileContexts  
            rowCount += 1
        #END line for loop


        #set connection to None so new connection can be established for potential other files
        self.connection.close()
        self.connection = None

        print( 'ENDING getFileContents' )
        return allFileContents
        


