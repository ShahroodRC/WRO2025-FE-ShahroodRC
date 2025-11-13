#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_2,INPUT_4,INPUT_3
from ev3dev2.sensor import Sensor, INPUT_1
from ev3dev2.sensor.lego import UltrasonicSensor,ColorSensor
from ev3dev2.motor import MediumMotor, OUTPUT_B, OUTPUT_D, SpeedPercent
from time import sleep
import time
import math
from ev3dev2.button import Button
from ev3dev2.led import Leds



rast = UltrasonicSensor(INPUT_2)
chap = UltrasonicSensor(INPUT_3)
color_sensor = ColorSensor(INPUT_4)
motor_a = MediumMotor(OUTPUT_B)
motor_b = MediumMotor(OUTPUT_D)
motor_a.reset() 




btn = Button()
leds = Leds()
leds.set_color('LEFT', 'ORANGE')
leds.set_color('RIGHT', 'ORANGE')


btn.wait_for_bump('enter')
leds.set_color('LEFT', 'GREEN')
leds.set_color('RIGHT', 'GREEN')

minDi=math.inf

def clamp(value, minimum, maximum):
    if value > maximum : value=maximum
    if value < minimum : value=minimum
    return value


def amotor(degrese,cl=50):
        diff =degrese
        diff=diff-motor_a.position
        diff=clamp(diff,-cl,cl)  

        motor_a.on(diff)


target = 45


a=0سلام! من فایل PDF قوانین عمومی WRO 2025 برای دسته‌بندی Future Engineers (Self-Driving Cars) رو کامل بررسی کردم. بخش‌های مرتبط با مستندات (documentation)، مهندسی ژورنال (Engineering Journal)، و گیت‌هاب (GitHub) عمدتاً در فصل ۷ (صفحات ۸-۹) و ضمیمه C (صفحات ۴۳-۴۶) هستن. این بخش‌ها توضیح می‌دن که تیم‌ها باید چه مستنداتی ارائه بدن، چطور از گیت‌هاب استفاده کنن، و چطور این مستندات امتیازدهی می‌شن.
من همه جزئیات رو به صورت کامل و ساختاربندی‌شده توضیح می‌دم. اگر چیزی نامفهوم بود، بگو تا بیشتر توضیح بدم. توجه کن که این قوانین برای مسابقات بین‌المللی هستن و ممکنه در مسابقات ملی کمی تغییر کنن (طبق قانون ۴.۳).
۱. الزامات کلی مستندات مهندسی (Engineer’s Documentation)
طبق فصل ۷ (Engineer’s documentation on GitHub)، مهندسی واقعی نه تنها درباره ساخت راه‌حل هست، بلکه درباره ارتباط و به اشتراک گذاشتن ایده‌ها با دیگران برای پیشرفت بیشتر. بنابراین، تیم‌ها علاوه بر طراحی و برنامه‌نویسی خودرو، باید مستنداتی ارائه بدن که پیشرفت مهندسی، طراحی نهایی خودرو، و کد منبع رو نشون بده.

محل ارائه مستندات:
باید روی یک مخزن عمومی (public repository) گیت‌هاب آپلود بشه.
یک نسخه چاپی (hardcopy) هم باید در فینال بین‌المللی تحویل داده بشه.
همه اطلاعات و مستندات روی گیت‌هاب باید به زبان انگلیسی باشن (برای مسابقات بین‌المللی).

محتویات الزامی که هر تیم باید ارائه بده:
بحث و توضیحات: اطلاعات، بحث، و انگیزه برای مدیریت تحرک (mobility)، قدرت و حسگرها (power and sense)، و مدیریت موانع (obstacle management). این بخش باید توضیح بده که چطور این جنبه‌ها طراحی شدن و چرا انتخاب شدن.
عکس‌ها:
عکس‌های خودرو از همه طرف‌ها (از هر سمت، بالا، و پایین).
یک عکس تیمی (team photo).

ویدیوهای عملکرد:
لینک به یوتیوب (عمومی یا قابل دسترسی با لینک).
ویدیو باید خودرو رو در حال رانندگی خودکار نشون بده.
بخش رانندگی باید حداقل ۳۰ ثانیه باشه.
یک ویدیو برای هر چالش (Open Challenge و Obstacle Challenge) الزامی هست.

لینک به مخزن گیت‌هاب عمومی:
شامل کد همه اجزایی که برنامه‌نویسی شدن (برای شرکت در مسابقه).
می‌تونه شامل فایل‌های مدل برای پرینترهای ۳بعدی، ماشین‌های برش لیزری، و CNC هم باشه (برای تولید قطعات خودرو).
تاریخچه کامیت‌ها (commits) باید حداقل ۳ کامیت داشته باشه:
کامیت اول: نه دیرتر از ۲ ماه قبل از مسابقه – باید حداقل ۱/۵ حجم کد نهایی رو داشته باشه.
کامیت دوم: نه دیرتر از ۱ ماه قبل از مسابقه.
کامیت سوم: نه دیرتر از ۲ هفته قبل از مسابقه.
کامیت‌های بیشتر مجاز هستن.

مخزن باید شامل فایل README.md باشه با توضیح کوتاه به انگلیسی (حداقل ۵۰۰۰ کاراکتر). هدف این توضیح:
توضیح ماژول‌های کد.
ارتباطشون با اجزای الکترومکانیکی خودرو.
فرآیند ساخت/کامپایل/آپلود کد به کنترلرهای خودرو.

یک الگو (template) برای مخزن گیت‌هاب موجوده: https://github.com/World-Robot-Olympiad-Association/wro2022-fe-template.
الزامات عمومی مخزن:
از لحظه ارسال برای مسابقه بین‌المللی باید عمومی باشه و حداقل ۱۲ ماه بعد از مسابقه عمومی بمونه.
هدف: تشویق تیم‌های جدید و الهام‌بخشی از راه‌حل‌های موجود.
اگر مخزن قبل از رویداد عمومی نباشه، امتیاز مستندات کم می‌شه.
انجمن WRO حق بازنشر مخزن رو داره.
مخزن‌ها باید برای مشاهده عمومی تنظیم بشن و محتوا قابل دیدن باشه.


کد روی گیت‌هاب و نسخه چاپی: باید با کامنت‌های خوب مستندسازی بشه. داورها ممکنه به برنامه‌های خاص (مثل EV3، Spike یا Scratch) دسترسی نداشته باشن، پس کامنت‌ها مهمن.

نکته مهم: ایده Future Engineers اینه که تیم‌های جدید رو تشویق کنه و بهشون کمک کنه تا از راه‌حل‌های موجود الهام بگیرن. اگر مخزن عمومی نباشه یا حذف بشه، WRO می‌تونه اون رو بازنشر کنه.

۲. امتیازدهی مستندات (Engineering Journal Evaluation)
طبق ضمیمه C (صفحات ۴۳-۴۶)، مستندات مهندسی (شامل گیت‌هاب) توسط حداقل ۳ داور ارزیابی می‌شن. امتیاز کل ۳۰ امتیاز داره و بر اساس ۸ حوزه زیر محاسبه می‌شه. هر داور جداگانه امتیاز می‌ده، بعد میانگین گرفته می‌شه، و مجموع میانگین‌ها امتیاز نهایی هست.

فرآیند ارزیابی:
حداقل ۳ داور مستندات رو بررسی می‌کنن.
هر داور برای هر حوزه امتیاز می‌ده (بدون بحث اولیه).
میانگین امتیاز هر حوزه محاسبه می‌شه.
مجموع میانگین‌ها = امتیاز کل مستندات.
امتیاز بر اساس درک داور از معیارها و احساسش نسبت به بازتاب معیارها در مستندات هست (نه مقایسه با تیم‌های دیگه).

مقیاس امتیاز (Rubric Scale) (برای همه حوزه‌ها یکسانه):
۰: هیچ مدرک یا بحثی ارائه نشده (Nothing provided).
۱: ناکافی (Too little information or information provided is not understood).
۲: نیاز به بهبود (Sufficient information is provided but it is clear that the effort cannot be duplicated).
۳: مطابق انتظارات (An exact duplication by another team can be made effortless from the information provided).
۴: فراتر از انتظارات (Not only can an exact duplication be made from the information provided, but information on improvements is also provided).

حوزه‌های امتیازدهی (با حداکثر امتیاز هر کدام):
Mobility Management (حداکثر ۴ امتیاز): بحث درباره مدیریت حرکت خودرو (موتورها، انتخاب و پیاده‌سازی‌شون، طراحی شاسی، اصول مهندسی مثل سرعت، گشتاور، قدرت). شامل دستورالعمل‌های ساخت و فایل‌های CAD 3D.
Power and Sense Management (حداکثر ۴ امتیاز): بحث درباره منبع قدرت و حسگرها (انتخاب حسگرها، مصرف قدرت، دیاگرام سیم‌کشی حرفه‌ای با BOM).
Obstacle Management (حداکثر ۴ امتیاز): بحث درباره استراتژی مدیریت موانع (برای همه چالش‌ها، شامل فلوچارت، pseudocode، و کد منبع با کامنت‌های دقیق).
Pictures – Team and vehicle (حداکثر ۴ امتیاز): عکس‌های تیم و خودرو (از همه طرف‌ها، واضح، مرتبط با بحث‌ها).
Performance videos (حداکثر ۴ امتیاز): ویدیوهای عملکرد (از شروع تا پایان هر چالش، حداقل ۳۰ ثانیه رانندگی، می‌تونه شامل کامنتاری، عنوان یا انیمیشن باشه).
GitHub utilization (حداکثر ۴ امتیاز): استفاده از گیت‌هاب برای مدیریت پروژه متن‌باز و کنترل نسخه فایل‌ها. امتیاز بر اساس کامل بودن اطلاعات، ساختار، و تعداد کامیت‌ها (چقدر پیشرفت رو نشون می‌ده). می‌تونه شامل اطلاعات اضافی درباره طراحی مهندسی و کد باشه.
Engineering Factor (حداکثر ۴ امتیاز): عامل مهندسی (چقدر خودرو طراحی و ساخته‌شده توسط تیم هست، نه فقط از کیت‌های آماده). مثلاً:
۰: هیچ توضیحی نداره.
۱: کیت RC یا مدولار آماده بدون تغییر.
۲: کیت آماده با تغییرات کم.
۳: کیت آماده با تغییرات طراحی و اجزای اضافه‌شده توسط تیم.
۴: طراحی و ساخت کامل توسط تیم، با اجزای الکتریکی آماده (مثل موتورها و حسگرها).

Overall Judge impression (حداکثر ۲ امتیاز):印象 کلی داورها (چقدر اطلاعات روی گیت‌هاب خوب ارتباط برقرار می‌کنه، طراحی و کد رو منتقل می‌کنه. آیا تلاش تیم قابل تکرار هست یا نه).
۰: ضعیف و ارتباط ضعیف (نمی‌شه تکرار کرد).
۱: متوسط (تکرار سخت هست).
۲: عالی (تکرار آسان هست).


نکته درباره گیت‌هاب در امتیازدهی: حوزه ۶ مستقیماً به استفاده از گیت‌هاب مربوط می‌شه. داورها چک می‌کنن که چقدر کامل، ساختاربندی‌شده، و منظم (با کامیت‌های مکرر) هست. اگر مخزن عمومی نباشه، امتیاز کم می‌شه (طبق فصل ۷).
نکته کلی امتیاز: امتیاز مستندات بخشی از امتیاز کل تیم هست (طبق فصل ۱۰: Scoring). امتیاز کل = امتیاز چالش‌ها + امتیاز مستندات (حداکثر ۳۰).

۳. نکات اضافی و عواقب عدم رعایت

اگر مستندات ناقص باشه یا گیت‌هاب عمومی نباشه، امتیاز کم می‌شه (فصل ۷).
طبق قانون ۳.۹، اگر مشکوک به کپی‌برداری باشه (مثل کد مشابه با دیگران)، ممکنه تیم جریمه بشه یا حذف بشه.
Q&A ممکنه قوانین رو تغییر بده، پس همیشه چک کن: https://wro-association.org/competition/questions-answers/.

این توضیح کامل هست بر اساس فایل.
g=0
cr1=color_sensor.color
while cr1 != 2 and cr1 != 5: 
    cr1=color_sensor.color
    motor_b.on(60)
while g != 60:
    motor_b.on(30)
    r=rast.distance_centimeters
    c=chap.distance_centimeters
    fr=(-2*(math.sqrt(11*(r))))+100
    fc=(-2*(math.sqrt(11*(c))))+100
    target=(fc*1.3)-(fr*1.7)
    print(target)
    amotor(clamp(target,-50,50))
    g=g+1
while True:
    if cr1==2 :
        while True:
            cr1=color_sensor.color
            if  cr1 == 2:
                while cr1==2:
                    cr1=color_sensor.color
                    motor_b.on_for_degrees(80, 70)
                    motor_a.stop(stop_action='coast')
                    motor_b.stop(stop_action='coast')



                a=a+1





            motor_b.on(60)
            distance = chap.distance_centimeters
            diff =((distance-27)*-2)
            diff=diff-motor_a.position  
            diff = clamp(diff ,-32,32)
            #motor_a.on(diff)
            amotor(diff)
            



            if a==11:
                i=0
                while i!=130:
                    motor_b.on(50)
                    distance = chap.distance_centimeters
                    diff =(distance-27)*-2
                    diff=diff-motor_a.position  
                    diff = clamp(diff ,-27,27)
                    amotor(diff)
                    i=i+1
                
                break
    elif cr1 ==  5 :  
        while True:
            cr1=color_sensor.color

            if cr1 == 5:
                while cr1==5:
                    cr1=color_sensor.color
                    motor_b.on_for_degrees(80, 70)
                    motor_a.stop(stop_action='coast')
                    motor_b.stop(stop_action='coast')
                    
                a=a+1





            motor_b.on(60)
            distance = rast.distance_centimeters
            diff =(distance-27)*2
            diff=diff-motor_a.position  
            diff = clamp(diff ,-32,32)
            amotor(diff)
            if a==11:  
                i=0
                while i!=130:
                    motor_b.on(50)
                    distance = rast.distance_centimeters
                    diff =(distance-27)*2
                    diff=diff-motor_a.position  
                    diff = clamp(diff ,-27,27)
                    amotor(diff)
                    i=i+1
                        
                break

    
            


            
    motor_b.off() 
    motor_a.off()
