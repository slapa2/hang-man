class Pictures:
    def __init__(self):
        self.hangmans = [
            '''		     
        
        
        
        
                           \n''',
            '''		     
        
        
        
        
                        _ _\n''',
            '''		     
                         |
                         |
                         |
                         |
                        _|_\n''',
            '''		      
                        \|
                         |
                         |
                         |
                        _|_\n''',
            '''		 ____
                        \|
                         |
                         |
                         |
                        _|_\n''',
            '''		 ____
                     |  \|
                         |
                         |
                         |
                        _|_\n''',
            '''		 ____
                     |  \|
                     o   |
                         |
                         |
                        _|_\n''',
            '''		 ____
                     |  \|
                     o   |
                     |   |
                         |
                        _|_\n''',

            '''		 ____
                     |  \|
                     o   |
                    /|\  |
                         |
                        _|_\n''',

            '''		 ____
                     |  \|
                     o   |
                    /|\  |
                    /\   |
                        _|_\n'''
        ]

    def getHangman(self, mishits):
        return self.hangmans[mishits]


