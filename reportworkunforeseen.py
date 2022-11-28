from Tools import tools_v000 as tools
import os
from os.path import dirname


# -20 for the name of this project reportWorkUnforeseen
save_path = os.path.dirname(os.path.abspath("__file__"))
propertiesFolder_path = save_path + "/"+ "Properties"

# Example of used
# user_text = tools.readProperty(propertiesFolder_path, 'reportWorkUnforeseen', 'user_text=')



# Aller a la page :
# https://app.myhours.com/?_ga=2.28119097.429480555.1601881225-847213319.1575362324#/reports/activity

# cliquer sur //*[@id="savedReportsButton"]

# cliquer sur le rapport de la date voulue
# //*[@id="activitySavedReportSelectDropDownMenu"]/li[2]/div/div[1]/button
# /html/body/div[1]/div/div/activity/div/app-navbar/div/div[3]/div/div[2]/activity-saved-reports-select/div/div/ul/li[2]/div/div[1]/button


# Doit pas oublier de valider pour chaque rows que c'est bien une date et pas le mois
# le mois
# //*[@id="activityGridContainer"]/div/div[6]/div/table/tbody/tr[1]

# La date
# //*[@id="activityGridContainer"]/div/div[6]/div/table/tbody/tr[2] 
# nombre d'heure passez sur le ticket de
# //*[@id="activityGridContainer"]/div/div[6]/div/table/tbody/tr[2]/td[12]/div/span

# le descriptif
# //*[@id="activityGridContainer"]/div/div[6]/div/table/tbody/tr[3]
# /html/body/div[1]/div/div/activity/div/div[3]/div/div/div/div[6]/div/table/tbody/tr[3]/td/div/div/div[1]/text-display/div/div/p

# La date
# //*[@id="activityGridContainer"]/div/div[6]/div/table/tbody/tr[4]

# le descriptif
# //*[@id="activityGridContainer"]/div/div[6]/div/table/tbody/tr[5]
# /html/body/div[1]/div/div/activity/div/div[3]/div/div/div/div[6]/div/table/tbody/tr[5]/td/div/div/div[1]/text-display/div/div/p


# Ouvrir l'url 
# https://jira.atlassian.insim.biz/browse/TOS-3087

# cliquer sur "More"
# //*[@id="opsbar-operations_more"]

# cliquer sur "Log work"
# //*[@id="log-work"]/a/span