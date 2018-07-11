import maya.cmds as cmds

cmds.file('D:/UCLA Academic/VCLA/Summer 2018/0710/0710/test/test.obj', i = True, type = 'OBJ', iv = True, ra = True, ns = 'test', mnc = True)
cmds.select('test:Mesh',r = True)
cmds.rename('test:Mesh' ,'Object1')

#center the pivot and freeze transformation
cmds.xform(cp = True)
cmds.setAttr('Object1.rx', -90)
cmds.move(-45, y = True)
cmds.makeIdentity('Object1', apply = True, t = 1, r = 1, s = 1, n = 0, pn = 1)

#reduce dimension
cmds.select('Object1',r = True)
cmds.polyReduce(ver = 1, p = 60.0)

#UV editor better use GUI







