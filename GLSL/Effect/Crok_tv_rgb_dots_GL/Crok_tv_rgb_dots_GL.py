# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Crok_tv_rgb_dots_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Crok_tv_rgb_dots_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Crok_tv_rgb_dots_GL"

def getLabel():
    return "Crok_tv_rgb_dots_GL"

def getVersion():
    return 1.1

def getIconPath():
    return "Crok_tv_rgb_dots_GL.png"

def getGrouping():
    return "Community/GLSL/Effect"

def getPluginDescription():
    return "Simulates the typical RGB dots of old TVs."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(1, 0.2353, 0.2353)

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("SETUP", "Setup")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.SETUP = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createIntParam("Shadertoy2paramValueInt0", "Cell size : ")
    param.setMinimum(1, 0)
    param.setMaximum(1000, 0)
    param.setDisplayMinimum(1, 0)
    param.setDisplayMaximum(1000, 0)
    param.setDefaultValue(9, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy2paramValueInt0 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createSeparatorParam("OPTIONS", "Options")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.OPTIONS = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createBooleanParam("isPremult", "Source is premultiplied : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.isPremult = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createStringParam("sep10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    param = lastNode.createSeparatorParam("MASK", "Mask")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.MASK = param
    del param

    param = lastNode.createStringParam("sep11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep11 = param
    del param

    param = lastNode.createStringParam("sep12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep12 = param
    del param

    param = lastNode.createBooleanParam("useMask", "Use mask : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Use mask input.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.useMask = param
    del param

    param = lastNode.createBooleanParam("invertMask", "Invert mask : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.invertMask = param
    del param

    param = lastNode.createChoiceParam("channelChoose", "Channel : ")
    entries = [ ("Red", ""),
    ("Green", ""),
    ("Blue", ""),
    ("Alpha", "")]
    param.setOptions(entries)
    del entries
    param.setDefaultValue("Alpha")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Channel used as mask.")
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.channelChoose = param
    del param

    param = lastNode.createStringParam("sep13", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep13 = param
    del param

    param = lastNode.createStringParam("sep14", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep14 = param
    del param

    param = lastNode.createSeparatorParam("MIX", "Mix")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.MIX = param
    del param

    param = lastNode.createStringParam("sep15", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep15 = param
    del param

    param = lastNode.createStringParam("sep16", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep16 = param
    del param

    param = lastNode.createDoubleParam("Dissolvewhich", "Mix : ")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Dissolvewhich = param
    del param

    param = lastNode.createStringParam("sep17", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep17 = param
    del param

    param = lastNode.createStringParam("sep18", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep18 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep101", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep101 = param
    del param

    param = lastNode.createStringParam("sep102", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep102 = param
    del param

    param = lastNode.createSeparatorParam("NAME", "Crok_tv_rgb_dots_GL v1.1")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NAME = param
    del param

    param = lastNode.createStringParam("sep103", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep103 = param
    del param

    param = lastNode.createStringParam("sep104", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep104 = param
    del param

    param = lastNode.createSeparatorParam("LINE101", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE101 = param
    del param

    param = lastNode.createStringParam("sep105", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep105 = param
    del param

    param = lastNode.createStringParam("sep106", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep106 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("sep107", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep107 = param
    del param

    param = lastNode.createStringParam("sep108", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep108 = param
    del param

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2019)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CONVERSION = param
    del param

    param = lastNode.createStringParam("sep109", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep109 = param
    del param

    param = lastNode.createStringParam("sep110", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep110 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 4487)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4137, 3418)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Shadertoy2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy2")
    lastNode.setLabel("Shadertoy2")
    lastNode.setPosition(4139, 3908)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy2 = lastNode

    param = lastNode.getParam("paramValueInt0")
    if param is not None:
        param.setValue(9, 0)
        del param

    param = lastNode.getParam("imageShaderFileName")
    if param is not None:
        param.setValue("/run/media/ffernandez/FABRICE/PERSO/NATRON/GIT_DEV/natron-plugins/Shadertoy/Crok_tv_rgb_dots.frag.glsl")
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n//\n//\n// Adaptation pour Natron par F. Fernandez\n// Code original : crok_tv_rgb_dots Matchbox pour Autodesk Flame\n\n// Adapted to Natron by F.Fernandez\n// Original code : crok_tv_rgb_dots Matchbox for Autodesk Flame\n\n\n// iChannel0: Source, filter = linear, wrap = mirror\n// BBox: iChannel0\n\n\nuniform int pCellsize = 9; // Cell size : (cell size), min=1, max=1000\n\n\n\n\n// RGB display\n// created by Daniil in 17/6/2013\n\nfloat CELL_SIZE_FLOAT = float(pCellsize);\nint RED_COLUMNS = int(CELL_SIZE_FLOAT/3.);\nint GREEN_COLUMNS = pCellsize-RED_COLUMNS;\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\n\tvec2 p = floor(fragCoord.xy / CELL_SIZE_FLOAT)*CELL_SIZE_FLOAT;\n\tint offsetx = int(mod(fragCoord.x,CELL_SIZE_FLOAT));\n\tint offsety = int(mod(fragCoord.y,CELL_SIZE_FLOAT));\n\n\tvec4 sum = texture2D(iChannel0, p / iResolution.xy);\n\t\n\tfragColor = vec4(0.,0.,0.,1.);\n\tif (offsety < pCellsize-1) {\t\t\n\t\tif (offsetx < RED_COLUMNS) fragColor.r = sum.r;\n\t\telse if (offsetx < GREEN_COLUMNS) fragColor.g = sum.g;\n\t\telse fragColor.b = sum.b;\n\t}\n\t\n}")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("wrap0")
    if param is not None:
        param.set("mirror")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source")
        del param

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("pCellsize")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Cell size :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("cell size")
        del param

    param = lastNode.getParam("paramDefaultInt0")
    if param is not None:
        param.setValue(9, 0)
        del param

    param = lastNode.getParam("paramMinInt0")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMaxInt0")
    if param is not None:
        param.setValue(1000, 0)
        del param

    del lastNode
    # End of node "Shadertoy2"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(4170, 3594)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Dissolve"
    lastNode = app.createNode("net.sf.openfx.DissolvePlugin", 1, group)
    lastNode.setScriptName("Dissolve")
    lastNode.setLabel("Dissolve")
    lastNode.setPosition(4139, 4246)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupDissolve = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(1, 0)
        del param

    del lastNode
    # End of node "Dissolve"

    # Start of node "Dot2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2")
    lastNode.setLabel("Dot2")
    lastNode.setPosition(4422, 3594)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2 = lastNode

    del lastNode
    # End of node "Dot2"

    # Start of node "Dot3"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot3")
    lastNode.setLabel("Dot3")
    lastNode.setPosition(4424, 4256)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot3 = lastNode

    del lastNode
    # End of node "Dot3"

    # Start of node "Shuffle1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Shuffle1")
    lastNode.setLabel("Shuffle1")
    lastNode.setPosition(4140, 3969)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1 = lastNode

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("A.uk.co.thefoundry.OfxImagePlaneColour.A")
        del param

    del lastNode
    # End of node "Shuffle1"

    # Start of node "Dot4"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot4")
    lastNode.setLabel("Dot4")
    lastNode.setPosition(4300, 3594)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot4 = lastNode

    del lastNode
    # End of node "Dot4"

    # Start of node "Dot5"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot5")
    lastNode.setLabel("Dot5")
    lastNode.setPosition(4300, 3983)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot5 = lastNode

    del lastNode
    # End of node "Dot5"

    # Start of node "Unpremult1"
    lastNode = app.createNode("net.sf.openfx.Unpremult", 2, group)
    lastNode.setScriptName("Unpremult1")
    lastNode.setLabel("Unpremult1")
    lastNode.setPosition(4139, 3841)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupUnpremult1 = lastNode

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Unpremult1"

    # Start of node "Premult1"
    lastNode = app.createNode("net.sf.openfx.Premult", 2, group)
    lastNode.setScriptName("Premult1")
    lastNode.setLabel("Premult1")
    lastNode.setPosition(4140, 4039)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupPremult1 = lastNode

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Premult1"

    # Start of node "Mask"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Mask")
    lastNode.setLabel("Mask")
    lastNode.setPosition(3508, 3342)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupMask = lastNode

    del lastNode
    # End of node "Mask"

    # Start of node "Shuffle1_2"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Shuffle1_2")
    lastNode.setLabel("Shuffle1_2")
    lastNode.setPosition(3486, 3983)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1_2 = lastNode

    param = lastNode.getParam("outputR")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.A")
        del param

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.A")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.A")
        del param

    del lastNode
    # End of node "Shuffle1_2"

    # Start of node "Alpha"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Alpha")
    lastNode.setLabel("Alpha")
    lastNode.setPosition(3662, 3736)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupAlpha = lastNode

    del lastNode
    # End of node "Alpha"

    # Start of node "Red"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Red")
    lastNode.setLabel("Red")
    lastNode.setPosition(3317, 3730)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupRed = lastNode

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.R")
        del param

    del lastNode
    # End of node "Red"

    # Start of node "Green"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Green")
    lastNode.setLabel("Green")
    lastNode.setPosition(3438, 3733)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupGreen = lastNode

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.G")
        del param

    del lastNode
    # End of node "Green"

    # Start of node "Blue"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Blue")
    lastNode.setLabel("Blue")
    lastNode.setPosition(3560, 3733)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupBlue = lastNode

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.B")
        del param

    del lastNode
    # End of node "Blue"

    # Start of node "SwitchChannel"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("SwitchChannel")
    lastNode.setLabel("SwitchChannel")
    lastNode.setPosition(3486, 3919)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitchChannel = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(3, 0)
        del param

    del lastNode
    # End of node "SwitchChannel"

    # Start of node "Crop"
    lastNode = app.createNode("net.sf.openfx.CropPlugin", 1, group)
    lastNode.setScriptName("Crop")
    lastNode.setLabel("Crop")
    lastNode.setPosition(3508, 3572)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupCrop = lastNode

    param = lastNode.getParam("rectangleInteractEnable")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(640, 0)
        param.setValue(480, 1)
        del param

    param = lastNode.getParam("reformat")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Crop"

    # Start of node "Blur1"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur1")
    lastNode.setLabel("Blur1")
    lastNode.setPosition(3508, 3464)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur1 = lastNode

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Blur1"

    # Start of node "Invert1"
    lastNode = app.createNode("net.sf.openfx.Invert", 2, group)
    lastNode.setScriptName("Invert1")
    lastNode.setLabel("Invert1")
    lastNode.setPosition(3486, 4148)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.48, 0.66, 1)
    groupInvert1 = lastNode

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Invert1"

    # Start of node "Dot6"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot6")
    lastNode.setLabel("Dot6")
    lastNode.setPosition(4010, 3594)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot6 = lastNode

    del lastNode
    # End of node "Dot6"

    # Start of node "Merge2"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge2")
    lastNode.setLabel("Merge2")
    lastNode.setPosition(4140, 4135)
    lastNode.setSize(80, 60)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge2 = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("copy")
        del param

    param = lastNode.getParam("enableMask_Mask")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Merge2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupDissolve)
    groupShadertoy2.connectInput(0, groupUnpremult1)
    groupDot1.connectInput(0, groupSource)
    groupDissolve.connectInput(0, groupDot3)
    groupDissolve.connectInput(1, groupMerge2)
    groupDot2.connectInput(0, groupDot4)
    groupDot3.connectInput(0, groupDot2)
    groupShuffle1.connectInput(0, groupShadertoy2)
    groupShuffle1.connectInput(1, groupDot5)
    groupDot4.connectInput(0, groupDot1)
    groupDot5.connectInput(0, groupDot4)
    groupUnpremult1.connectInput(0, groupDot1)
    groupPremult1.connectInput(0, groupShuffle1)
    groupShuffle1_2.connectInput(0, groupSwitchChannel)
    groupAlpha.connectInput(0, groupCrop)
    groupRed.connectInput(0, groupCrop)
    groupGreen.connectInput(0, groupCrop)
    groupBlue.connectInput(0, groupCrop)
    groupSwitchChannel.connectInput(0, groupRed)
    groupSwitchChannel.connectInput(1, groupGreen)
    groupSwitchChannel.connectInput(2, groupBlue)
    groupSwitchChannel.connectInput(3, groupAlpha)
    groupCrop.connectInput(0, groupBlur1)
    groupBlur1.connectInput(0, groupMask)
    groupInvert1.connectInput(0, groupShuffle1_2)
    groupDot6.connectInput(0, groupDot1)
    groupMerge2.connectInput(0, groupPremult1)
    groupMerge2.connectInput(1, groupDot6)
    groupMerge2.connectInput(2, groupInvert1)

    param = groupShadertoy2.getParam("paramValueInt0")
    group.getParam("Shadertoy2paramValueInt0").setAsAlias(param)
    del param
    param = groupDissolve.getParam("which")
    group.getParam("Dissolvewhich").setAsAlias(param)
    del param
    param = groupUnpremult1.getParam("disableNode")
    param.setExpression("not thisGroup.isPremult.get()", False, 0)
    del param
    param = groupPremult1.getParam("disableNode")
    param.setExpression("not thisGroup.isPremult.get()", False, 0)
    del param
    param = groupSwitchChannel.getParam("which")
    param.setExpression("thisGroup.channelChoice.get()", False, 0)
    del param
    param = groupCrop.getParam("size")
    param.setExpression("myWidth = Blur1.getOutputFormat().width()\nret = myWidth", True, 0)
    param.setExpression("myHeight = Blur1.getOutputFormat().height()\nret = myHeight", True, 1)
    del param
    param = groupInvert1.getParam("disableNode")
    param.setExpression("thisGroup.invertMask.get()", False, 0)
    del param
    param = groupMerge2.getParam("disableNode")
    param.setExpression("not thisGroup.useMask.get()", False, 0)
    del param

    try:
        extModule = sys.modules["Crok_tv_rgb_dots_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
