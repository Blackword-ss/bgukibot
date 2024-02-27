from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import Update
from telegram.ext import CallbackContext

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f"Привет, {user.first_name}! выбери язык для получения информации. \nHi, {user.first_name}! please choose the language to continue. ",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Русский язык", callback_data='rus')],
            [InlineKeyboardButton("English language", callback_data='eng')],
        ]))

# Обработчик команды
def language_button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == 'eng':
        keyboard = [
            [InlineKeyboardButton("Contact information", callback_data='contact')],
            [InlineKeyboardButton("Admission Procedure", callback_data='admission')],
            [InlineKeyboardButton("Training period", callback_data='training')],
            [InlineKeyboardButton("Choose your programme", callback_data='programme')],
            [InlineKeyboardButton("Language of study", callback_data='language')],
            [InlineKeyboardButton("Payment Details", callback_data='payment')],
            [InlineKeyboardButton("Faculties", callback_data='faculties')],
            [InlineKeyboardButton("Accommodation", callback_data='accommodation')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Choose to see inforamtion:", reply_markup=reply_markup)
    elif query.data == 'rus':
        keyboard = [
            [InlineKeyboardButton("Контактная информация", callback_data='contact_ru')],
            [InlineKeyboardButton("Порядок приёма документов", callback_data='admission_ru')],
            [InlineKeyboardButton("Подготовительные курсы", callback_data='training_ru')],
            [InlineKeyboardButton("Выбор специальности", callback_data='programme_ru')],
            [InlineKeyboardButton("Языки обучения", callback_data='language_ru')],
            [InlineKeyboardButton("Детали оплаты за обучение", callback_data='payment_ru')],
            [InlineKeyboardButton("Факультеты", callback_data='faculties_ru')],
            [InlineKeyboardButton("Общежитие", callback_data='accommodation_ru')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Выберете пункт для получения информации:", reply_markup=reply_markup)


# Обработчик нажатия на кнопку
def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == 'contact':
        query.edit_message_text(text="Department for International Cooperation \n Address: 17 Rabkorovskaya Str., Minsk, 220007 \n Tel. +375 17 352-83-71\n E-mail: buk@buk.by\n www.buk.by\n Tel.  +375 17 375-20-00\n +375 17 374-83-50\n +375 17 270-37-01\n E-mail: comm@buk.by\n E-mail: bukinterdep@yahoo.com")
    elif query.data == 'admission':
        keyboard = [
            [InlineKeyboardButton("Documents and Cost", callback_data='cost')],
            [InlineKeyboardButton("Apply to University", callback_data='apply')],
            [InlineKeyboardButton("Documents for admission", callback_data='admissiondocs')],
            [InlineKeyboardButton("Registration Information", callback_data='registration')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Here is the admission procedure:", reply_markup=reply_markup)
    elif query.data == 'training':
        keyboard = [
            [InlineKeyboardButton("Preparatory department", callback_data='preparatory')],
            [InlineKeyboardButton("Bachelor degree", callback_data='bachelor')],
            [InlineKeyboardButton("Master degree", callback_data='master')],
            [InlineKeyboardButton("Postgraduate", callback_data='postgraduate')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Please choose the training period:", reply_markup=reply_markup)
    elif query.data == 'programme':
        keyboard = [
            [InlineKeyboardButton("Preparatory department", callback_data='pp')],
            [InlineKeyboardButton("Bachelor degree", callback_data='pb')],
            [InlineKeyboardButton("Master degree", callback_data='pm')],
            [InlineKeyboardButton("Postgraduate", callback_data='ppt')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Please choose the study programm:", reply_markup=reply_markup)
    elif query.data == 'language':
        keyboard = [
            [InlineKeyboardButton("Bachelor degree", callback_data='lb')],
            [InlineKeyboardButton("Master degree", callback_data='lm')],
            [InlineKeyboardButton("Postgraduate", callback_data='lp')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Please choose your degree:", reply_markup=reply_markup)
    elif query.data == 'payment':
        query.edit_message_text(text="The is a payment details...")
    elif query.data == 'faculties':
        keyboard = [
            [InlineKeyboardButton("Cultural Studies and Sociocultural Activities", callback_data='fkiskd')],
            [InlineKeyboardButton("Information and Document Communications", callback_data='fidk')],
            [InlineKeyboardButton("Art Culture", callback_data='fhk')],
            [InlineKeyboardButton("Music and Choreographic Art", callback_data='fmhi')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Please choose the faculty:", reply_markup=reply_markup)
    elif query.data == 'accommodation':
        query.edit_message_text(text="- There are two student hostels located nearby academic buildings \n - Foreign students usually live in double rooms \n - Student hostels are equipped with all necessary furniture to live in comfort. There are large common rooms and study halls as well as laundries, kitchens and gyms \n - Hobby clubs function on a regular basis. A lot of cultural events and concerts are held in the Student Residential Complex")
    
    
    
    #####################   Русский язык  ################################
   
   
   
    elif query.data == 'contact_ru':
        query.edit_message_text(text="Отдел международных отношений \nАдрес: ул. Рабкоровская 17, Минск, 220007 \nТел. +375 17 352-83-71 \nE-mail: buk@buk.by \nwww.buk.by \nТел.  +375 17 375-20-00 \n+375 17 374-83-50 \n+375 17 270-37-01 \nE-mail: comm@buk.by \nE-mail: bukinterdep@yahoo.com")
    elif query.data == 'admission_ru':
        keyboard = [
            [InlineKeyboardButton("Документы и оплата", callback_data='cost_ru')],
            [InlineKeyboardButton("Поступление в университет", callback_data='apply_ru')],
            [InlineKeyboardButton("Документы для поступления", callback_data='admissiondocs_ru')],
            [InlineKeyboardButton("Информация для регистрации", callback_data='registration_ru')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Информация для поступающих:", reply_markup=reply_markup)
    elif query.data == 'training_ru':
        keyboard = [
            [InlineKeyboardButton("Подготовительное отделение", callback_data='preparatory_ru')],
            [InlineKeyboardButton("Бакалавриат", callback_data='bachelor_ru')],
            [InlineKeyboardButton("Магистратура", callback_data='master_ru')],
            [InlineKeyboardButton("Аспирантура", callback_data='postgraduate_ru')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Выберите ступень для подготовки:", reply_markup=reply_markup)
    elif query.data == 'programme_ru':
        keyboard = [
            [InlineKeyboardButton("Подготовительное отделение", callback_data='pp_ru')],
            [InlineKeyboardButton("Бакалавриат", callback_data='pb_ru')],
            [InlineKeyboardButton("Магистратура", callback_data='pm_ru')],
            [InlineKeyboardButton("Аспирантура", callback_data='ppt_ru')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Выберите программу обучения:", reply_markup=reply_markup)
    elif query.data == 'language_ru':
        keyboard = [
            [InlineKeyboardButton("Бакалавриат", callback_data='lb_ru')],
            [InlineKeyboardButton("Магистратура", callback_data='lm_ru')],
            [InlineKeyboardButton("Аспирантура", callback_data='lp_ru')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Выберите своё образование:", reply_markup=reply_markup)
    elif query.data == 'payment_ru':
        query.edit_message_text(text="Тут должны быть детали оплаты....")
    elif query.data == 'faculties_ru':
        keyboard = [
            [InlineKeyboardButton("Факультет культурологии и социально-культурной деятельности", callback_data='fkiskd_ru')],
            [InlineKeyboardButton("Факультет информационно-документных коммуникаций", callback_data='fidk_ru')],
            [InlineKeyboardButton("Факультет художественной культуры", callback_data='fhk_ru')],
            [InlineKeyboardButton("Факультет музыкального и хореографического искусства", callback_data='fmhi_ru')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Выберите факультет:", reply_markup=reply_markup)
    elif query.data == 'accommodation_ru':
        query.edit_message_text(text="- Рядом расположены два студенческих общежития \n - Иностранные студенты обычно живут в двухместных номерах \n - Студенческие общежития оснащены всей необходимой мебелью, чтобы жить в комфорте.Есть большие общие комнаты и учебные залы, а также прачечные, кухни и спортивные залы \n - Хобби -клубы функционируют на регулярной основе.Много культурных мероприятий и концертов проводится в студенческом жилом комплексе")






# Обработчик кнопки Language of study
def language_button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == 'lb':
        query.edit_message_text(text="Russian")
    elif query.data == 'lm':
        query.edit_message_text(text="English/Russian")
    elif query.data == 'lp':
        query.edit_message_text(text="Russian")
    
################### РУССКИЙ ЯЗЫК ##########################

    elif query.data == 'lb_ru':
        query.edit_message_text(text="Русский язык")
    elif query.data == 'lm_ru':
        query.edit_message_text(text="Английский и русский язык")
    elif query.data == 'lp_ru':
        query.edit_message_text(text="Русский язык")







# Обработчик кнопки Training period
def training_button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == 'preparatory':
        query.edit_message_text(text="9 month...")
    elif query.data == 'bachelor':
        query.edit_message_text(text="4 years...")
    elif query.data == 'master':
        query.edit_message_text(text="1 year...")
    elif query.data == 'postgraduate':
        query.edit_message_text(text="5 years...")
   
################### РУССКИЙ ЯЗЫК ##########################

    elif query.data == 'preparatory_ru':
        query.edit_message_text(text="9 месяцев...")
    elif query.data == 'bachelor_ru':
        query.edit_message_text(text="4 года...")
    elif query.data == 'master_ru':
        query.edit_message_text(text="1 год...")
    elif query.data == 'postgraduate_ru':
        query.edit_message_text(text="5 лет..")




# Обработчик кнопки Choose your programme
def programm_button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == 'pp':
        query.edit_message_text(text="Тут пока ничего нет...А должно?")
    elif query.data == 'pb':
        query.edit_message_text(text="Musical Folk Instrumental Arts \nVariety Musical Art Chorcographic Art \nFolk Singing Art \nChoral Arts \nComputer Music \nLibrary and Information Activity \nMuseum Studies and Protection of Historical and Cultural Heritage \nCultural Studies \nSocial and Cultural Management and Communications \nSocial and Cultural Activities \nArt History \nApplied Arts \nPerformances and Holiday Direction \nTheater Direction")
    elif query.data == 'pm':
        query.edit_message_text(text="Art History \nCultural studics \nArts Management \nSocial and Cultural Studies \nLibrary and Information Studies \nMuseum Studies and Protection of Historical and Cultural Heritage")
    elif query.data == 'ppt':
        query.edit_message_text(text="Тут пока ничего нет...А должно?")
   
################### РУССКИЙ ЯЗЫК ##########################

    elif query.data == 'pp_ru':
        query.edit_message_text(text="Тут пока ничего нет...А должно?")
    elif query.data == 'pb_ru':
        query.edit_message_text(text="Музыкальное народное инструментальное искусство \nЭстрадное музыкальное искусство Хореографическое искусство \nНародное певческое искусство \nХоровое искусство \nКомпьютерная музыка \nБиблиотечно-информационная деятельность \nМузееведение и охрана исторического и культурного наследия \nКультурология \nСоциально-культурный менеджмент и коммуникации \nСоциально-культурная деятельность \nИстория искусств \nПрикладное искусство \nПостановка спектаклей и праздников \nТеатральная режиссура")
    elif query.data == 'pm_ru':
        query.edit_message_text(text="История искусств \nКультурология \nХудожественный менеджмент \nСоциокультурные исследования \nБиблиотечно-информационные исследования \nМузееведение и охрана исторического и культурного наследия")
    elif query.data == 'ppt_ru':
        query.edit_message_text(text="Тут пока ничего нет...А должно?")
            





# Обработчик кнопки Admission Procedure
def admission_button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == 'cost':
        query.edit_message_text(text= "To study in the Republic of Belarus, you need a student visa.\n It's necessary to obtain an invitation letter before the arrival and get a student visa at the nearest diplomatic mission of the Republic of Belarus. \n NOTE! Make sure that you inform the Department for International Cooperation about the time of your arrival in Belarus as well as the necessity of providing you with accommodation in the student residence beforehand.\n • Medical insurance — 200 USD;\n • Medical examination — 75 USD;\n • Registration of an exit visa — 25 USD;\n • Registration of temporary stay — 15 USD;\n • Registration of temporary residence (for 1 year) — 40 USD;\n • Translation of documents (if necessary) — from 50 USD;\n • Accommodation in the student residence — 50 USD (per month).\nAll foreign citizens arriving to study at the University should contact the Department for International Cooperation (room 316, +375 17 3758350,) within three days after crossing the border of the Republic of Belarus." )  
    elif query.data == 'apply':
        query.edit_message_text(text="After arriving in Belarus, you should contact the Department for International Cooperation of Belarusian State University of Culture and Arts (room 302, +375 17 3752000, +375 29 7546224, WeChat, Viber, WhatsApp, Telegram) and provide the package of documents specified in your invitation letter. Make sure that all the documents are translated into Russian or Belarusian and certified by a notary. After that, the specialists of the Department will inform you about an interview with university professors. The interview can be conducted in English or Russian (depending on the chosen language of study). Admission interviews are conducted to assess the skills required in educational process and depend on the chosen programme.")
    elif query.data == 'admissiondocs':
        query.edit_message_text(text="Bachelor degree: \n - the original of the diploma of secondary education with the application, issued in the Republic of Belarus, or a document on education issued in a foreign state, which indicates the studied disciplines and their volume, marks (points) received on them; \n - the conclusion of the medical consulting commission issued by the territorial health organization of the Republic of Belarus;\n - a medical report on the state of health and a certificate of absence of HIV infection, issued by the official health authority of the country from which the candidate came from;\n - duly certified copy of the birth certificate;\n - duly certified copy of the passport;\n - 4 photos 3x4 cm;\n - 2 photos 2x3 cm.\n All documents should have a notarized translation into one of the state languages of the Republic of Belarus (Belarusian or Russian). \n\nMaster degree:\n- the original of the diploma of higher education with the application, issued in the Republic of Belarus, or a document on education issued in a foreign state, which indicates the studied disciplines and their volume, marks (points) received on them;\n - the conclusion of the medical consulting commission issued by the territorial health organization of the Republic of Belarus;\n - a medical report on the state of health and a certificate of absence of HIV infection, issued by the official health authority of the country from which the candidate came from;\n - duly certified copy of the birth certificate\n - 4 photos 3x4 cm;\n - 2 photos 2x3 cm.\n All documents should have a notarized translation into one of the state languages of the Republic of Belarus (Belarusian or Russian)")
    elif query.data == 'registration':
        query.edit_message_text(text="Upon arrival in the Republic of Belarus, a foreign citizen must apply to the Department for international cooperations to sign a study agreement and register a temporary stay. You can also register a temporary stay on your own on the Unified Portal of E-services portal.gov.by (registration is free): procedure 200.12.14.1 'Registration of a foreign citizen or stateless person temporarily staying in the Republic of Belarus'.\n For registration of temporary residence (for up to 1 year), a foreign citizen must provide the following documents to the Department for international cooperation:\n 1. Passport;\n 2. Notarized passport translation into Russian;\n 3. A copy of the previous temporary residence permit or a copy of the visa (for new arrivals);\n 4. Insurance policy;\n 5. Study agreement;\n 6. Rental agreement for a flat or dormitory;\n 7. Application form (the form is issued by a department employee);\n 8. Payment receipt (banking details are issued by a department officer).")
    
################### РУССКИЙ ЯЗЫК ##########################

    elif query.data == 'cost_ru':
        query.edit_message_text(text= "Чтобы учиться в Республике Беларусь, вам нужна студенческая виза.\n Необходимо получить пригласительное письмо до прибытия и получить студенческую визу на ближайшей дипломатической миссии Республики Беларусь. \n ПРИМЕЧАНИЕ! Убедитесь, что вы сообщите Департаменту о международном сотрудничестве о времени вашего прибытия в Беларусь, а также о необходимости предоставления вам жилья в студенческой резиденции.\n • Медицинское страхование - 200 долларов США;\n • Медицинское обследование - 75 долларов США;\n • Регистрация выхода визы - 25 долларов США;\n • Регистрация временного пребывания - 15 долларов США;\n • Регистрация временного места жительства (на 1 год) - 40 долларов США;\n • Перевод документов (при необходимости) - от 50 долларов США;\n • Размещение в студенческой резиденции - 50 долларов США (в месяц).\nВсе иностранные граждане, прибывающие для обучения в университете, должны связаться с департаментом международного сотрудничества (комната 316, +375 17 3758350) в течение трех дней после пересечения границы Республики Беларусь." )  
    elif query.data == 'apply_ru':
        query.edit_message_text(text="После прибытия в Беларусь вы должны связаться с департаментом международного сотрудничества Беларусского государственного университета культуры и искусств (кабинет 302, +375 17 3752000, +375 29 7546224, WeChat, Viber, WhatsApp, Telegram) и предоставление пакета документов, указанных в вашем приглашении. Убедитесь, что все документы переведены на русский или белорусский язык и сертифицированны нотариусом. После этого специалисты департамента сообщут вам о интервью с профессорами университетов.Интервью может проводиться на английском или русском языке (в зависимости от выбранного языка обучения).Приемные интервью проводятся для оценки навыков, необходимых в образовательном процессе, и зависят от выбранной программы.")
    elif query.data == 'admissiondocs_ru':
        query.edit_message_text(text="Cтепень бакалавра: \n - Оригинал диплома среднего образования с заявлением, выпущенным в Республике Беларусь, или документ по образованию, выпущенному в иностранном государстве, который указывает на изученные дисциплины и их объем, отметки (очки), полученные за них; \n - заключение Комиссии по медицинской консалтингу, выпущенной территориальной организацией здравоохранения Республики Беларусь;\n - Медицинский отчет о состоянии здоровья и свидетельство о отсутствии ВИЧ -инфекции, выпущенное официальным управлением здравоохранения страны, из которого кандидат прибыл;\n - должным образом сертифицированная копия свидетельства о рождении;\n - должным образом сертифицированная копия паспорта;\n - 4 фото 3х4 см;\n - 2 фотографии 2x3 см.\n Все документы должны иметь нотариоцированный перевод на один из государственных языков Республики Беларусь (беларусский или русский). \n\nСтепень магистра:\n- Оригинал диплома высшего образования с заявлением, выпущенным в Республике Беларусь, или документ по образованию, выпущенному в иностранном государстве, который указывает на изученные дисциплины и их объем, полученные на них знаки (баллы);\n - Заключение Комиссии по медицинской консультации, выпущенной Организацией территориальной здравоохранения Республики Беларусь;\n - Медицинский отчет о состоянии здоровья и свидетельство о отсутствии ВИЧ -инфекции, выпущенное официальным управлением здравоохранения страны, из которого кандидат прибыл;\n - должным образом сертифицированная копия свидетельства о рождении\n - 4 фото 3х4 см;\n - 2 фотографии 2x3 см.\n Все документы должны иметь нотариоцированный перевод на один из государственных языков Республики Беларусь (белорусская или русская)")
    elif query.data == 'registration_ru':
        query.edit_message_text(text="По прибытии в Республику Беларусь иностранный гражданин должен обратиться в Департамент по международным кооперациям, чтобы подписать соглашение об обучении и зарегистрировать временное пребывание.Вы также можете зарегистрировать временное пребывание самостоятельно на Unified Portal of E-услуги Portal.gov.by (регистрация бесплатна): Процедура 200.12.14.1 'Регистрация иностранного гражданина или без гражданства, временно оставшегося в Республике Беларусь.\n Для регистрации временного проживания (на срок до 1 года) иностранный гражданин должен предоставить следующие документы Департаменту для международного сотрудничества:\n 1. Заграничный пасспорт;\n 2. Нотаризированный перевод паспорта на русский;\n 3. Копия предыдущего разрешения на проживание или копия визы (для вновь прибывших);\n 4. Страховой полис;\n 5. Учебное соглашение;\n 6. Соглашение об аренде для квартиры или общежития;\n 7. Форма заявления (форма выдается сотрудником департамента);\n 8. Квитанция о оплате (банковские данные выдаются сотрудником департамента).")






# Главная функция
def main() -> None:
    token = "6512472196:AAHdciVuAtedAkr2mGzheS6n69vT31Rlu6s"
    updater = Updater( token , use_context=True)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(language_button, pattern='eng|rus'))

    updater.dispatcher.add_handler(CallbackQueryHandler(button_click, pattern='accommodation|faculties|payment|programme|training|admission|contact|language|accommodation_ru|faculties_ru|payment_ru|programme_ru|training_ru|admission_ru|contact_ru|language_ru'))
    updater.dispatcher.add_handler(CallbackQueryHandler(training_button_click, pattern='preparatory|bachelor|master|postgraduate|preparatory_ru|bachelor_ru|master_ru|postgraduate_ru'))
    updater.dispatcher.add_handler(CallbackQueryHandler(admission_button_click, pattern='cost|apply|admissiondocs|registration|cost_ru|apply_ru|admissiondocs_ru|registration_ru'))
    updater.dispatcher.add_handler(CallbackQueryHandler(language_button_click, pattern='lb|lm|lp|lb_ru|lm_ru|lp_ru'))
    updater.dispatcher.add_handler(CallbackQueryHandler(programm_button_click, pattern='pp|pb|pm|ppt|pp_ru|pb_ru|pm_ru|ppt_ru'))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
