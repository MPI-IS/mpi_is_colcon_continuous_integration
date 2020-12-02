import os
import tempfile


class Workspace:

    """
    class for managing the workspace directory,
    i.e. the folder in which repositories will
    be cloned and source code will be compiled. 

    :param str path: if a string, the desired path to the work
    directory (will be created if does not exist). If None,
    a temp directory will be used
    """
    
    def __init__(self,path):

        # using a user defined directory
        if path is not None:
            os.makedirs(path)
            self._path = path
            self._tmp = False

        # using a temp directory
        else:
            self._f = tempfile.TemporaryDirectory()
            self._path = self._f.name
            self._tmp = True


    
    def get_files(self,subdir,suffix):

        """
        Walk the directory path/subdir
        and returns a list of the absolute paths
        of all *suffix files found.
        """

        root = self._f+os.sep+subdir
        found = []
        
        for root,dirs,files in os.walk(root):
            for f in files:
                found.extend([root+os.sep+f for f in files
                              if f.endswith(suffix)])

        return found

        
