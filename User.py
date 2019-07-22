class User
    """
    Class that generates new instance
    """
    user_list = [] #Empty user list
    
    def __init__(self,idNo,username,password):
        self.id = idNo
        self.user = username
        self.psw = password