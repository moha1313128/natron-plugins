# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Guides_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Guides_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Guides_GL"

def getLabel():
    return "Guides_GL"

def getVersion():
    return 1.0

def getIconPath():
    return "Guides_GL.png"

def getGrouping():
    return "Community/GLSL/Draw"

def getPluginDescription():
    return "Draws simple adjustable horizontal and vertical guides for centering reference, measuring, etc..."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

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

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool0", "Enable Horizontal : ")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool0 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool1", "Enable Vertical : ")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool1 = param
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
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createSeparatorParam("WIDTH_HEIGHT", "Width & Height")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.WIDTH_HEIGHT = param
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

    param = lastNode.createIntParam("Shadertoy1_2paramValueInt2", "Width : ")
    param.setMinimum(0, 0)
    param.setMaximum(4096, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(4096, 0)
    param.setDefaultValue(1728, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueInt2 = param
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

    param = lastNode.createIntParam("Shadertoy1_2paramValueInt3", "Height : ")
    param.setMinimum(0, 0)
    param.setMaximum(3112, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(3112, 0)
    param.setDefaultValue(972, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueInt3 = param
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

    param = lastNode.createDoubleParam("offsetX", "Offset x : ")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(-500, 0)
    param.setDisplayMaximum(500, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.offsetX = param
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

    param = lastNode.createDoubleParam("offsetY", "Offset y : ")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(-500, 0)
    param.setDisplayMaximum(500, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.offsetY = param
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

    param = lastNode.createSeparatorParam("GUIDE_PROPERTIES", "Guide properties")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.GUIDE_PROPERTIES = param
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

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat6", "Guides opacity : ")
    param.setMinimum(0, 0)
    param.setMaximum(99.99999999999999, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(99.99999999999999, 0)
    param.setDefaultValue(100, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat6 = param
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

    param = lastNode.createColorParam("Shadertoy1_2paramValueVec35", "Guides color : ", False)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)
    param.setDefaultValue(1, 1)
    param.restoreDefaultValue(1)
    param.setDefaultValue(1, 2)
    param.restoreDefaultValue(2)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueVec35 = param
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

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool7", "Draw thicker : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool7 = param
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

    param = lastNode.createSeparatorParam("NAME", "Guides_GL v1.0")

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

    param = lastNode.createSeparatorParam("LINE01", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE01 = param
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

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2018)")

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
    lastNode.setPosition(4139, 4048)
    lastNode.setSize(90, 50)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4139, 3645)
    lastNode.setSize(90, 50)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Shadertoy1_2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1_2")
    lastNode.setLabel("Shadertoy1_2")
    lastNode.setPosition(4139, 3842)
    lastNode.setSize(90, 50)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1_2 = lastNode

    param = lastNode.getParam("paramValueBool0")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool1")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueInt2")
    if param is not None:
        param.setValue(1728, 0)
        del param

    param = lastNode.getParam("paramValueInt3")
    if param is not None:
        param.setValue(972, 0)
        del param

    param = lastNode.getParam("paramValueVec24")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    param = lastNode.getParam("paramValueVec35")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(1, 2)
        del param

    param = lastNode.getParam("paramValueFloat6")
    if param is not None:
        param.setValue(99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramValueBool7")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n//\n//\n// Adaptation pour Natron par F. Fernandez\n// Code original : id_Guidance Matchbox pour Autodesk Flame\n\n// Adapted to Natron by F.Fernandez\n// Original code : id_Guidance Matchbox for Autodesk Flame\n\n\n// setting inputs names and filtering options\n// iChannel0: Source, filter = nearest\n// BBox: iChannel0\n\n\n// Guidance (C)2017 Bob Maple\n// bobm-matchbox [at] idolum.com\n\n\n\nuniform bool enable_h = true; // Enable Horizontal : \nuniform bool enable_v = true; // Enable Vertical : \n\nuniform int amount_h = 1728; // Width : , min=0, max=4096\nuniform int amount_v = 972; // Height : , min=0, max=3112\n\n\nuniform vec2 offset_xy = vec2(0.0,0.0); // Guides offset : (X/Y Offset Amount)\nuniform vec3 guide_color = vec3(1.0,1.0,1.0); // Guides color : \nuniform float guide_trans = 100.0; // Guides opacity : , min=0.0, max=100.0\nuniform bool thicker = false; // Draw thicker : \n\n\n\n\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\n    // Convert pixel coords to UV position for texture2D\n    // and fetch the input pixel into px\n\n    vec2 uv  = fragCoord.xy / vec2( iResolution.x, iResolution.y );\n    vec4 px  = vec4( texture2D( iChannel0, uv ).rgb, 1.0 );\n\n    // Figure out where to draw the guides\n\n    float guide_rx = (iResolution.x / 2.0) + (amount_h / 2.0);\n    float guide_lx = (iResolution.x / 2.0) - (amount_h / 2.0 - 1);\n\n    float guide_uy = (iResolution.y / 2.0) + (amount_v / 2.0);\n    float guide_ly = (iResolution.y / 2.0) - (amount_v / 2.0 - 1);\n\n    // Add the guide offsets\n\n    guide_rx += floor(offset_xy[0]);\n    guide_lx += floor(offset_xy[0]);\n\n    guide_uy += floor(offset_xy[1]);\n    guide_ly += floor(offset_xy[1]);\n\n    // Draw the guides\n\n\tif( enable_v ) {\n\n\t\tif( floor(fragCoord.x) == guide_lx || floor(fragCoord.x) == guide_rx )\n\t\t\tpx = vec4( mix( px, vec4( guide_color, 1.0 ), (guide_trans / 100.0) ) );\n\n\t\tif( thicker )\n\t\t\tif( floor(fragCoord.x) == guide_lx-1 || floor(fragCoord.x) == guide_rx+1 )\n\t\t\t\tpx = vec4( mix( px, vec4( guide_color, 1.0 ), (guide_trans / 100.0) ) );\n\t}\n\n\tif( enable_h ) {\n\n\t\tif( floor(fragCoord.y) == guide_uy || floor(fragCoord.y) == guide_ly )\n        \tpx = vec4( mix( px, vec4( guide_color, 1.0 ), (guide_trans / 100.0) ) );\n\n\t\tif( thicker )\n\t\t\tif( floor(fragCoord.y) == guide_uy+1 || floor(fragCoord.y) == guide_ly-1 )\n\t        \tpx = vec4( mix( px, vec4( guide_color, 1.0 ), (guide_trans / 100.0) ) );\n\t}\n\n\tfragColor = px;\n}\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("wrap0")
    if param is not None:
        param.set("clamp")
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

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(8, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("enable_h")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Enable Horizontal :")
        del param

    param = lastNode.getParam("paramDefaultBool0")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("enable_v")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Enable Vertical :")
        del param

    param = lastNode.getParam("paramDefaultBool1")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("amount_h")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Width :")
        del param

    param = lastNode.getParam("paramDefaultInt2")
    if param is not None:
        param.setValue(1728, 0)
        del param

    param = lastNode.getParam("paramMinInt2")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxInt2")
    if param is not None:
        param.setValue(4096, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("amount_v")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("Height :")
        del param

    param = lastNode.getParam("paramDefaultInt3")
    if param is not None:
        param.setValue(972, 0)
        del param

    param = lastNode.getParam("paramMinInt3")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxInt3")
    if param is not None:
        param.setValue(3112, 0)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("vec2")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("offset_xy")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("Guides offset :")
        del param

    param = lastNode.getParam("paramHint4")
    if param is not None:
        param.setValue("X/Y Offset Amount")
        del param

    param = lastNode.getParam("paramType5")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName5")
    if param is not None:
        param.setValue("guide_color")
        del param

    param = lastNode.getParam("paramLabel5")
    if param is not None:
        param.setValue("Guides color :")
        del param

    param = lastNode.getParam("paramDefaultVec35")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(1, 2)
        del param

    param = lastNode.getParam("paramType6")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName6")
    if param is not None:
        param.setValue("guide_trans")
        del param

    param = lastNode.getParam("paramLabel6")
    if param is not None:
        param.setValue("Guides opacity :")
        del param

    param = lastNode.getParam("paramDefaultFloat6")
    if param is not None:
        param.setValue(99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramMinFloat6")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat6")
    if param is not None:
        param.setValue(99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType7")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName7")
    if param is not None:
        param.setValue("thicker")
        del param

    param = lastNode.getParam("paramLabel7")
    if param is not None:
        param.setValue("Draw thicker :")
        del param

    del lastNode
    # End of node "Shadertoy1_2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy1_2)
    groupShadertoy1_2.connectInput(0, groupSource)

    param = groupShadertoy1_2.getParam("paramValueBool0")
    group.getParam("Shadertoy1_2paramValueBool0").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool1")
    group.getParam("Shadertoy1_2paramValueBool1").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueInt2")
    group.getParam("Shadertoy1_2paramValueInt2").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueInt3")
    group.getParam("Shadertoy1_2paramValueInt3").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueVec24")
    param.setExpression("thisGroup.offsetX.get()", False, 0)
    param.setExpression("thisGroup.offsetY.get()", False, 1)
    del param
    param = groupShadertoy1_2.getParam("paramValueVec35")
    group.getParam("Shadertoy1_2paramValueVec35").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat6")
    group.getParam("Shadertoy1_2paramValueFloat6").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool7")
    group.getParam("Shadertoy1_2paramValueBool7").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["Guides_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
