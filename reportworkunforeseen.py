from Tools import tools_v000 as tools
import os
from os.path import dirname


# -20 for the name of this project reportWorkUnforeseen
save_path = os.path.dirname(os.path.abspath("__file__"))
propertiesFolder_path = save_path + "/"+ "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'reportWorkUnforeseen', 'user_text=')



# Ouvrir un 