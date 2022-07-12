import time
import keyboard
import pyautogui


def start_1v():
    company = False
    finaly_load = False
    pyautogui.screenshot('screen\\worksreen.png')
    screen = pyautogui.locateOnScreen('screen\\1c.png', confidence=0.9)
    pyautogui.doubleClick('screen\\1c.png')

    while not company:
        pyautogui.screenshot('screen\\worksreen.png')
        time.sleep(3)
        company = pyautogui.locateOnScreen('screen\\1c.png', confidence=0.9)

    pyautogui.click('screen\\enter_company.png')

    """
    Ожидание полной загрузки 1с
    """
    while not finaly_load:
        pyautogui.screenshot('screen\\worksreen.png')
        time.sleep(3)
        finaly_load = pyautogui.locateOnScreen('screen\\service.png', confidence=0.9)

    print('1c готова к работе')


def open_entera():
    global updates
    update = 0
    time.sleep(3)
    pyautogui.screenshot('screen\\worksreen.png')
    pyautogui.locateOnScreen('screen\\service.png', confidence=0.9)  # найти кнопку Сервис
    pyautogui.doubleClick('screen\\service.png')

    time.sleep(2)
    pyautogui.screenshot('screen\\worksreen.png')
    pyautogui.locateOnScreen('screen\\additional external reports and processing.png', confidence=0.9)
    # найти кнопку 'дополнительные внешние отчеты и обработки' в Сервис
    pyautogui.click('screen\\additional external reports and processing.png')

    time.sleep(3)
    pyautogui.screenshot('screen\\worksreen.png')
    pyautogui.locateOnScreen('screen\\processing.png', confidence=0.9)  # найти кнопку Сервис
    pyautogui.click('screen\\processing.png')

    time.sleep(3)
    pyautogui.screenshot('screen\\worksreen.png')
    pyautogui.locateOnScreen('screen\\entera load 2021.png', confidence=0.9)
    pyautogui.doubleClick('screen\\entera load 2021.png')

    while not update:
        waiting_time = 0
        pyautogui.screenshot('screen\\worksreen.png')
        update = pyautogui.locateOnScreen('screen\\update.png', confidence=0.9)
        if update is None and waiting_time != 10:
            waiting_time = waiting_time + 1
        elif waiting_time == 10:
            update = True
            print("Не загрузился список обновлений")
        elif update:
            pyautogui.locateOnScreen('screen\\update_close.png', confidence=0.9)
            pyautogui.doubleClick('screen\\update_close.png')
            print('Загрузился список обновлений, робот закрыл')


def recognize_documents():
    pyautogui.screenshot('screen\\worksreen.png')
    pyautogui.locateOnScreen('screen\\recognize documents.png', confidence=0.9)  # найти кнопку Распознать документы
    pyautogui.doubleClick('screen\\recognize documents.png')
    time.sleep(1)
    keyboard.write(
        'C:\\Users\\rpabank\\Documents\\Rparobot\\20062022-102122\\2.pdf')  # почему то pyautogui отказывается вставлять кирилицу в строку
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.screenshot('screen\\worksreen.png')
    pyautogui.locateOnScreen('screen\\button_recognize_documents.png',
                             confidence=0.9)  # найти кнопку Распознать документы
    pyautogui.doubleClick('screen\\button_recognize_documents.png')


def greate_docks():
    time.sleep(1)
    on_recognition = True # На распознавании
    recognition_finaly = False # Распознан
    while on_recognition and not recognition_finaly: # пока на распознавании и не распознан
        pyautogui.screenshot('screen\\worksreen.png')
        on_recognition = pyautogui.locateOnScreen('screen\\on recognition.png', confidence=0.9)
        recognition_finaly = pyautogui.locateOnScreen('screen\\recognized.png', confidence=0.9)
        print("Документ на распознавании")

    pyautogui.screenshot('screen\\worksreen.png')
    ss = pyautogui.locateOnScreen('screen\\highlight.png', confidence=0.9)
    if not ss:
        ss = pyautogui.locateOnScreen('screen\\highlight_color.png', confidence=0.9)
    click = pyautogui.center(ss)
    pyautogui.click(click) # Поставить галочку на против первого документа

    pyautogui.locateOnScreen('screen\\greate_dock.png', confidence=0.9)
    pyautogui.click('screen\\greate_dock.png') # Нажать "Создать документ"

    pyautogui.press('enter') # Выбирается первый пункт из выпадающего списка
    existence_check()
    check_type_dock()


def check_type_dock():
    item_nomenclature = False
    pyautogui.screenshot('screen\\worksreen.png')
    transport_services = pyautogui.locateOnScreen('screen\\transport services.png', confidence=0.9)
    transport_services_green = pyautogui.locateOnScreen('screen\\transport services_green.png', confidence=0.9)
    Delivery_Services = pyautogui.locateOnScreen('screen\\Delivery Services.png', confidence=0.9)
    if transport_services and not Delivery_Services:
        pyautogui.locateOnScreen('screen\\product.png', confidence=0.9)
        pyautogui.doubleClick('screen\\product.png') # в колонке Тип элемента найти и дважды нажать на "Товар"

        pyautogui.screenshot('screen\\worksreen.png')
        pyautogui.locateOnScreen('screen\\change to service.png', confidence=0.9)
        pyautogui.click('screen\\change to service.png')# в колонке Тип элемента сменить на "Услуга"

        pyautogui.screenshot('screen\\worksreen.png')
        pyautogui.locateOnScreen('screen\\field element 1s.png', confidence=0.9)
        pyautogui.doubleClick('screen\\field element 1s.png') # ищет соседнее поле в колонке "Элемент в 1с"

        keyboard.write('Услуги по доставке груза покупателю')
        pyautogui.press('enter')
        pyautogui.press('enter')

        pyautogui.screenshot('screen\\worksreen.png')
        pyautogui.locateOnScreen('screen\\Delivery Services 9300.png', confidence=0.9)
        pyautogui.doubleClick('screen\\Delivery Services 9300.png') # выбрать "Услуги по доставке груза покупателю B000009300(номер не точный), всегда выбирать с ндс

        while not item_nomenclature:
            pyautogui.screenshot('screen\\worksreen.png')
            item_nomenclature = pyautogui.locateOnScreen('screen\\item nomenclature.png', confidence=0.9)
            print('ищем окно номенклатуры')

        print('окно номенклатуры найдено')

    elif transport_services_green and Delivery_Services:
        pyautogui.locateOnScreen('screen\\product_green.png', confidence=0.9)
        pyautogui.doubleClick('screen\\product_green.png')

        pyautogui.screenshot('screen\\worksreen.png')
        pyautogui.locateOnScreen('screen\\change to service.png', confidence=0.9)
        pyautogui.click('screen\\change to service.png')

        pyautogui.locateOnScreen('screen\\greate_dock_in_directory_elements.png', confidence=0.9)
        pyautogui.click('screen\\greate_dock_in_directory_elements.png')
    elif not transport_services:
        print('Не нашел тип услуги')


def existence_check():
    time.sleep(2)
    pyautogui.screenshot('screen\\worksreen.png')
    recreate_documents = pyautogui.locateOnScreen('screen\\recreate documents.png', confidence=0.9)
    duplicates_found = pyautogui.locateOnScreen('screen\\duplicates found.png', confidence=0.9)
    if recreate_documents:
        pyautogui.press('enter')
    elif duplicates_found:
        pyautogui.click('screen\\link documents.png')
        pyautogui.screenshot('screen\\worksreen.png')
        recreate_documents = pyautogui.locateOnScreen('screen\\recreate documents.png', confidence=0.9)
        if recreate_documents:
            pyautogui.press('enter')