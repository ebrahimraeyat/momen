import PySide2
from PySide2 import QtCore, QtGui
import FreeCAD
import FreeCADGui
import DraftTools
import os
import column_types
import column_type
import section
import update


def QT_TRANSLATE_NOOP(ctx, txt): return txt


class Dxf:
    def Activated(self):
        filename = get_save_filename('.dxf')
        if not filename:
            return
        import techdraw
        techdraw.export_to_dxf(filename)

    def IsActive(self):
        return True if FreeCADGui.ActiveDocument else False

    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            "Dxf",
            "Export to Dxf")
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            "Dxf",
            "Export to Dxf")
        rel_path = "Mod/SteelColumn/Resources/icons/Dxf.svg"
        path = FreeCAD.ConfigGet("AppHomePath") + rel_path
        import os
        if not os.path.exists(path):
            path = FreeCAD.ConfigGet("UserAppData") + rel_path
        return {'Pixmap': path,
                'MenuText': MenuText,
                'ToolTip': ToolTip}

class Levels:

    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            "Levels",
            "Creates Levels")
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            "Levels",
            "Creates Levels")
        rel_path = "Mod/SteelColumn/Resources/icons/Levels.svg"
        path = FreeCAD.getHomePath() + rel_path
        import os
        if not os.path.exists(path):
            path =  FreeCAD.getUserAppDataDir() + rel_path
        return {'Pixmap': path,
                'MenuText': MenuText,
                'ToolTip': ToolTip}


    def  Activated(self):
        column_types.create_levels()

    def IsActive(self):
        return True if FreeCADGui.ActiveDocument else False


class Columns:

    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            "Levels",
            "Creates Columns")
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            "Levels",
            "Creates Columns")
        rel_path = "Mod/SteelColumn/Resources/icons/add.svg"
        path = FreeCAD.getHomePath() + rel_path
        import os
        if not os.path.exists(path):
            path =  FreeCAD.getUserAppDataDir() + rel_path
        return {'Pixmap': path,
                'MenuText': MenuText,
                'ToolTip': ToolTip}


    def  Activated(self):
        column_type.create_columns()

    def IsActive(self):
        return True if FreeCADGui.ActiveDocument.Levels else False


class RemoveColumn:
    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            "Levels",
            "Remove Columns")
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            "Levels",
            "Remove Columns")
        rel_path = "Mod/SteelColumn/Resources/icons/remove.svg"
        path = FreeCAD.getHomePath() + rel_path
        import os
        if not os.path.exists(path):
            path =  FreeCAD.getUserAppDataDir() + rel_path
        return {'Pixmap': path,
                'MenuText': MenuText,
                'ToolTip': ToolTip}


    def  Activated(self):
        column_type.remove_column()

    def IsActive(self):
        return True if FreeCADGui.ActiveDocument.Levels else False


class Sections:

    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            "Sections",
            "Creates Sections")
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            "Sections",
            "Creates Sections")
        rel_path = "Mod/SteelColumn/Resources/icons/section.svg"
        path = FreeCAD.getHomePath() + rel_path
        import os
        if not os.path.exists(path):
            path =  FreeCAD.getUserAppDataDir() + rel_path
        return {'Pixmap': path,
                'MenuText': MenuText,
                'ToolTip': ToolTip}


    def  Activated(self):
        section.create_sections()

    def IsActive(self):
        return True if FreeCADGui.ActiveDocument.Levels else False


class Update:

    def GetResources(self):
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            "Update",
            "Update")
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            "Update",
            "Update Steel Column WorkBench")
        rel_path = "Mod/SteelColumn/Resources/icons/update.png"
        path = FreeCAD.getHomePath() + rel_path
        import os
        if not os.path.exists(path):
            path =  FreeCAD.getUserAppDataDir() + rel_path
        return {'Pixmap': path,
                'MenuText': MenuText,
                'ToolTip': ToolTip}


    def  Activated(self):
        update.update()

    def IsActive(self):
        return True



def get_save_filename(ext):
    from PySide2.QtWidgets import QFileDialog
    filters = f"{ext[1:]} (*{ext})"
    filename, _ = QFileDialog.getSaveFileName(None, 'select file',
                                              None, filters)
    if not filename:
        return
    if not ext in filename:
        filename += ext
    return filename


FreeCADGui.addCommand("steel_column_levels", Levels())
FreeCADGui.addCommand("steel_column_section", Sections())
FreeCADGui.addCommand("steel_column_columns", Columns())
FreeCADGui.addCommand("steel_column_remove", RemoveColumn())
FreeCADGui.addCommand('steel_column_dxf', Dxf())
FreeCADGui.addCommand("steel_column_update", Update())

steel_column_commands = [
    "steel_column_levels",
    "steel_column_section",
    "steel_column_columns",
    "steel_column_remove",
    "steel_column_dxf",
    "steel_column_update",
    ]
