from Util import materialType


class MaterialManager:

    def __init__(self, params: list):
        self.params = params
        # other configurations

    def changeMaterial(self, material) -> bool:
        returnText = ""
        textBaseForValidMaterial = "Material is changed to"

        match material:
            case materialType.Titanium:
                self.carManager.setMaterial(materialType.Titanium)
                returnText = textBaseForValidMaterial + " Titanium."

            case materialType.Carbon:
                self.carManager.setMaterial(materialType.Carbon)
                returnText = textBaseForValidMaterial + " Carbon."


            case materialType.AlloyX:
                self.carManager.setMaterial(materialType.AlloyX)
                returnText = textBaseForValidMaterial + " AlloyX."

                
            case _:
                returnText = "Material seletion is invalid."

        return self._announceMaterial(returnText)

    def _announceMaterial(self, text: str) -> bool:
        returnValue = False
         try:
             returnValue = self.announcer(text)
         except:
            print("Announcement of material type is failed.")
            returnValue = False
        finally:
            return returnValue
