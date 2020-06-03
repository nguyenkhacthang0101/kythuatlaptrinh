class Nguoi(object):
    def GetGender( self ):
        return "Unknown"

class Nam( Nguoi ):
    def GetGender( self ):
        return "Nam"

class Nu ( Nguoi ):
    def GetGender( self ):
        return "Nu"

aNam = Nam()
aNu = Nu()
print (aNam.GetGender())
print (aNu.GetGender())
