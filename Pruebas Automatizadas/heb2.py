from __future__ import print_function
from selenium import webdriver
from os.path import join, dirname, abspath
import xlrd
from xlrd.sheet import ctype_text
import time

class heb_productos(object):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://www.heb.com.mx/")

        self.fname = join(dirname(dirname(abspath(__file__))), 'untitled',
                          'heblista.xlsx')
        self.xl_workbook = xlrd.open_workbook(self.fname)

        # List sheet names, and pull a sheet by name
        #
        self.sheet_names = self.xl_workbook.sheet_names()
        self.xl_sheet = self.xl_workbook.sheet_by_name(self.sheet_names[0])

        self.row = self.xl_sheet.row(0)  # 1st row

        self.arreglo2 = []
        self.arreglo3 = []
        self.arreglo = self.arreglo2, self.arreglo3
        self.contador3 = 0

        for self.idx, self.cell_obj in enumerate(self.row):
            self.cell_type_str = ctype_text.get(self.cell_obj.ctype,
                                                'unknown type')

        # Print all values, iterating through rows and columns
        #
        self.num_cols = self.xl_sheet.ncols  # Number of columns
        for self.row_idx in range(0,
                                  self.xl_sheet.nrows):  # Iterate through rows
            self.contador3 += 1
            for self.col_idx in range(0, self.num_cols):
                # Iterate through columns
                self.cell_obj = self.xl_sheet.cell(self.row_idx,
                                                   self.col_idx).value
                # Get cell object by row, col
                print(self.cell_obj)
                if self.contador3 == 1:
                    self.arreglo2.append(self.cell_obj)
                if self.contador3 == 2:
                    self.arreglo3.append(self.cell_obj)
    def productosheb(self):
        for f in range(0, 2):
            department = str(self.arreglo[f][0])
            Productonom = str(self.arreglo[f][1])
            cant = str(self.arreglo[f][2])
            subitem = str(self.arreglo[f][3])

            print(department)

            element = self.driver.find_element_by_css_selector(".tittle"
                                                               "-info>h1")
            assert element.text == 'Recomendación de la semana'

            txt = self.driver.find_element_by_css_selector(".tittle-info>h1").text
            txt1 = self.driver.find_element_by_css_selector(".cont-info>h2").text
            concat = "La " + txt + " es : " + txt1
            print(concat)
            departamento = self.driver.find_elements_by_xpath("id('select-categories')"
                                                         "/option")
            for i in departamento:
                if i.text == department:
                    i.click()

            buscador = self.driver.find_element_by_css_selector("#search")
            buscador.send_keys(Productonom)
            buscador.submit()

            time.sleep(10)
            # validar = driver.find_element_by_xpath(".//*[@id='top']/body
            # /div[1]/div/div[4]/div/div[2]/div[2]/div[1]/h1").text
            # print (validar)
            # if validar == "resultados de la
            # búsqueda para '"+Productonom+"'":
            #   print("validado")

            ordlista = self.driver.find_element_by_xpath(".//*[@id='top']/body/"
                                                    "div[1]/div/div[4]/div/"
                                                    "div[2]/div[2]/div[2]/"
                                                    "div[1]/div[2]/p[1]/a")
            ordlista.click()

            time.sleep(7)

            precio = self.driver.find_elements_by_xpath(".//*[@id='top']/body/"
                                                   "div[1]/div/div[4]/div/"
                                                   "div[2]/div[2]/div[2]/"
                                                   "div[1]/div[2]/div[1]/"
                                                   "div/select/option")
            for x in precio:
                if x.text == "Precio ▼":
                    x.click()
                    break

            contador = 1
            productlist = self.driver.find_elements_by_xpath(".//*[@id='products-list']/li")
            for n in range(1, len(productlist)):
                p = str(n)
                link = ".//*[@id='products-list']/li[" + p + "]/div[2]/div/div[2]/h2/a"
                producto = self.driver.find_elements_by_xpath(link)
                compra = self.driver.find_elements_by_css_selector(".qty")
                for x in producto:
                    if x.text == subitem:
                        variable = x.text
                        for c in compra:
                            if contador == n:
                                c.clear()
                                c.send_keys(cant)
                                c.submit()

                            contador += 1

                n += 1
            time.sleep(8)

            close = self.driver.find_element_by_xpath(".//*[@id='closeBtn']")
            close.click()
            time.sleep(8)
            validar2 = self.driver.find_element_by_xpath(".//*[@id='top']/body/"
                                                    "div[1]/div/div[4]/div/"
                                                    "div[2]/"
                                                    "div[2]/ul[2]/li/ul/li").text
            if validar2 == variable + " se agregó al carrito.":
                print("validado")

            carritoblanco = self.driver.find_element_by_xpath(".//*[@id='gotocar']"
                                                         "/div/a/span[3]")
            if carritoblanco.text == cant:
                print("carrito igual a 2")

            carrito = self.driver.find_element_by_xpath(".//*[@id='gotocar']/div/a/span[1]")
            carrito.click()

            carritocompra = self.driver.find_element_by_xpath(".//*[@id='btnMinicart']")
            carritocompra.click()
            ronda = str(f)
            print("ronda " + ronda)

            f += 1
            self.driver.delete_all_cookies()
            self.driver.get("https://www.heb.com.mx/")
            if f == 2:
                self.driver.save_screenshot('screenie.png')
                self.driver.quit()


