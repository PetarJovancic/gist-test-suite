class Utilities():
    ### Global variables
    input_path = 'C:\gist_test_suite\gist_test_suite\input_files'
    output_path = 'C:\gist_test_suite\gist_test_suite\output_files'
    url="https://api.github.com"                                       ### REST API URL
    user="PetarJovancic"                                               ### Username
    __token_Unauthorized='16951b3d98bdfg11c5c61e6ce2degfe8bdh'         ### Unauthorized Access
    __token_Public='16951b3d98b11c5c61e6ce2dee99a493abce8bdb'          ### Public Access
    __token_Authorized='bd079f53e3c207d65a606e0c848cb077c1c1d7ed'      ### Authorized Access

    ### Folder structure
    import os
    def folder_structure(self):
        try:
            self.output_files = self.os.mkdir(self.output_path)
        except OSError:
            self.output_files = self.output_path
        self.output_files = self.output_path
        self.input_files = self.input_path
        return self.output_files,self.input_files

    ### Type of token
    def token_type(self):
        while True:
            self.type_of_authorization = input("Please choose the type of authorization (Unauthorized, Public or Authorized): ")
            if self.type_of_authorization == "Unauthorized":
                self.token=self.__token_Unauthorized
                break
            elif self.type_of_authorization =="Public":
                self.token=self.__token_Public
                break
            elif self.type_of_authorization=="Authorized":
                self.token = self.__token_Authorized
                break
        return self.token
