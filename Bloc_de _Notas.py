#Trabajo Interfaz y bloc de notas
import os
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import * 
import sys
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.path=None
        self.ancho = 800
        self.alto = 500
        self.posicionIzquierda = 100
        self.posicionArriba= 100 

        self.setGeometry(self.posicionIzquierda, self.posicionArriba, self.ancho, self.alto)
        self.setWindowTitle("Programa")

        #Barra de estado
        self.statusBar().showMessage("Bienvenid@")

        

        #Menu
        menu = self.menuBar()

        #Campo de Texto
        self.editor = QPlainTextEdit()

        Contenedor_V= QVBoxLayout()   #Contenedor Vertical

        Contenedor_V.addWidget(self.editor) 
  
        Contenedor = QWidget() 
  
        Contenedor.setLayout(Contenedor_V) 
        
        self.setCentralWidget(Contenedor) 

        self.barra_de_estado = QStatusBar() 
  
        
        self.setStatusBar(self.barra_de_estado) 
  
        
        edicion_barra_de_estado = QToolBar("Edicion") 
  
        
        self.addToolBar(edicion_barra_de_estado) 


        #Fuente 
        fuente_fija = QFontDatabase.systemFont(QFontDatabase.FixedFont) 
        fuente_fija.setPointSize(12) 
        self.editor.setFont(fuente_fija) 


        #Elementos del Menu
        menu_archivo=menu.addMenu("Archivo")
        

        menu_archivo_abrir = QAction("Abrir...", self)
        menu_archivo.addAction(menu_archivo_abrir)
        menu_archivo_abrir.setStatusTip("Abrir")
        menu_archivo_abrir.triggered.connect(self.MenuArchivoAbrir) #Lanzador

        menu_archivo_guardar = QAction("Guardar", self)
        menu_archivo.addAction(menu_archivo_guardar)
        menu_archivo_guardar.setStatusTip("Guardar la página actual")
        menu_archivo_guardar.triggered.connect(self.MenuArchivoGuardar) #Lanzador
        
        menu_archivo_guardar_como = QAction("Guardar como...", self)
        menu_archivo.addAction(menu_archivo_guardar_como)
        menu_archivo_guardar_como.setStatusTip("Guardar la página actual en el archivo especificado")
        menu_archivo_guardar_como.triggered.connect(self.MenuArchivoGuardarComo) #Lanzador

        menu_archivo_imprimir = QAction("Imprimir", self)    
        menu_archivo.addAction(menu_archivo_imprimir) 
        menu_archivo_imprimir.setStatusTip("Imprimir la pagina actual")
        menu_archivo_imprimir.triggered.connect(self.MenuArchivoImprimir) 



        menu_edicion=self.menuBar().addMenu("Edicion") 


        menu_edicion_deshacer = QAction("Deshacer", self)    
        menu_edicion.addAction(menu_edicion_deshacer) 
        menu_edicion_deshacer.setStatusTip("Deshacer el último cambio")
        menu_edicion_deshacer.triggered.connect(self.editor.undo)
        edicion_barra_de_estado.addAction(menu_edicion_deshacer) 
        
        menu_edicion_rehacer = QAction("Rehacer", self)    
        menu_edicion.addAction(menu_edicion_rehacer) 
        menu_edicion_rehacer.setStatusTip("Rehacer el último cambio")
        menu_edicion_rehacer.triggered.connect(self.editor.redo)
        edicion_barra_de_estado.addAction(menu_edicion_rehacer) 

        menu_edicion_cortar = QAction("Cortar", self)    
        menu_edicion.addAction(menu_edicion_cortar) 
        menu_edicion_cortar.setStatusTip("Cortar texto seleccionado")
        menu_edicion_cortar.triggered.connect(self.editor.cut)
        edicion_barra_de_estado.addAction(menu_edicion_cortar)

        menu_edicion_copiar = QAction("Copiar", self)    
        menu_edicion.addAction(menu_edicion_copiar) 
        menu_edicion_copiar.setStatusTip("Copiar texto seleccionado")
        menu_edicion_copiar.triggered.connect(self.editor.copy)
        edicion_barra_de_estado.addAction(menu_edicion_copiar)

        menu_edicion_pegar = QAction("Pegar", self)    
        menu_edicion.addAction(menu_edicion_pegar) 
        menu_edicion_pegar.setStatusTip("Pegar texto seleccionado")
        menu_edicion_pegar.triggered.connect(self.editor.paste)
        edicion_barra_de_estado.addAction(menu_edicion_pegar) 

        menu_edicion_seleccionar_todo = QAction("Seleccionar todo", self)    
        menu_edicion.addAction(menu_edicion_seleccionar_todo) 
        menu_edicion_seleccionar_todo.setStatusTip("Seleccionar todo ")
        menu_edicion_seleccionar_todo.triggered.connect(self.editor.selectAll)
        edicion_barra_de_estado.addAction(menu_edicion_seleccionar_todo)  


        menu_ver=menu.addMenu("Ver")
        menu_ver_accion_ajustar = QAction("Ajustar texto de la ventana", self) 
        menu_ver_accion_ajustar.setStatusTip("Marque para ajustar el texto a la ventana") 
        menu_ver_accion_ajustar.setCheckable(True) 
        menu_ver_accion_ajustar.setChecked(True) 
        menu_ver_accion_ajustar.triggered.connect(self.MenuVerAccionAjustar) 
        menu_ver.addAction(menu_ver_accion_ajustar) 


        
        #Detectar Caracteres 
        self.editor.textChanged.connect(self.MenuVerActualizarDato)
        

        #Actualizar Titulo 
        self.actualizar_titulo()
        









    def dialog_critical(self, s): 
  
        
        dlg = QMessageBox(self) 
  
        
        dlg.setText(s) 
  
        
        dlg.setIcon(QMessageBox.Critical) 
  
        
        dlg.show() 


    
    def MenuArchivoAbrir(self): 
  
        
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "",  
                             "Text documents(*.txt);All files(*.*)") 
  
        
        if path: 
            
            try: 
                with open(path, 'rU') as f: 
                    
                    text = f.read() 
  
            
            except Exception as e: 
  
                
                self.dialog_critical(str(e)) 
            
            else: 
                
                self.path = path 
  
                
                self.editor.setPlainText(text) 
  
                
                self.actualizar_titulo()
        

    def MenuArchivoGuardar(self): 
  
        
        if self.path is None: 
  
            
            return self.MenuArchivoGuardarComo() 
  
        
        self._guardar_en_path(self.path) 

    def actualizar_titulo(self): 
        
        self.setWindowTitle("%s - PyQt5 Bloc de Notas" %(os.path.basename(self.path)  if self.path else "Untitled"))  
    
    def MenuArchivoGuardarComo(self): 

  
        
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "",  
                             "Text documents(*.txt);All files(*.*)") 
  
        
        if not path: 
            
            
            return
  
        
        self._guardar_en_path(path) 


    def _guardar_en_path(self, path): 
  
        
        text = self.editor.toPlainText() 
  
        
        try: 
  
            
            with open(path, 'w') as f: 
  
                
                f.write(text) 
  
        
        except Exception as e: 
  
            
            self.dialog_critical(str(e)) 
  
        
        else: 
            
            self.path = path 
            
            self.actualizar_titulo() 

    def MenuArchivoImprimir(self): 
        
        dlg = QPrintDialog() 
        
        if dlg.exec_(): 
            
            self.editor.print_(dlg.printer())
        
    def MenuVerAccionAjustar(self): 
  
        
        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0 ) 
    
    def MenuVerActualizarDato(self):
        self.valor_texto=self.editor.toPlainText()
        self.caracteres=str(self.valor_texto)
        self.mostrar=len(self.caracteres)
        self.statusBar().showMessage("Caracteres: "+str(self.mostrar), 1000)
        


  
   

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    codigoDeFinalizacion = app.exec_()
    sys.exit(codigoDeFinalizacion)