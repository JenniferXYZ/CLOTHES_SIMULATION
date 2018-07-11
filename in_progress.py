import maya.cmds as cmds

for panel in cmds.getPanel(sty="graphEditor") or []:
    cmds.scriptedPanel(panel, e=True, to=True)