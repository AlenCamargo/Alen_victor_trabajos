;;;SE para recomendar una rutina de ejercicios a una persona

(defrule inicio
=>

(printout t "¡Bienvenido!" crlf)
(printout t "Este sistema te ayudará a elegir una rutina de ejercicios dependiendo de tu condicion!!" crlf)





(printout t "Por favor, ingresa tu edad: ")
  (bind ?edad (read))
  (assert  (edad ?edad))


(printout t "Por favor, ingresa tu altura (en metros): ")
  (bind ?altura (read))
  (assert  (altura ?altura))


   (printout t "Por favor, ingresa tu peso (en kg): ")
  (bind ?peso (read))
  (assert  (peso ?peso))
  
  (printout t "¿Cuál es tu nivel de condición física? (bajo/medio/alto): ")
  (bind ?nivel (read))
  (assert  (nivel-condicion-fisica ?nivel))
  

 (printout t "¿Cuál es tu tipo de genética? (mesomorfo/ectomorfo/endomorfo): ")
  (bind ?genetica (read))
  (assert  (tipo-genetica ?genetica))


     (printout t "¿Cuál es tu objetivo? (perder-peso/ganar-masa-muscular/mantener-forma): ")
  (bind ?objetivo (read))
  (assert  (objetivo ?objetivo))


  (printout t "¿Tienes preferencia por algún tipo de ejercicio? (cardio/fuerza): ")
  (bind ?preferencia (read))
  (assert  (preferencia-ejercicio ?preferencia))


(printout t "Por favor, especifica un grupo muscular que deseas enfocar (pecho, espalda, brazos, hombros, muslos, pantorrillas): ")
  (bind ?grupo-muscular (read))
  (assert (grupo-muscular ?grupo-muscular))

 

(printout t "¿Prefieres entrenar en casa?  si,no " crlf)
(bind ?lugar-entrenamiento (read))
(assert (lugar-entrenamiento ?lugar-entrenamiento))


)








;;;Definicion de reglas

;;;Definir regla para calcular el IMC

(defrule calcular-almacenar-imc
   (altura ?altura)
   (peso ?peso)
   =>
   (bind ?imc (/ ?peso (* ?altura ?altura)))
   (assert (IMC ?imc)))




;;;Definir regla para recomendar segun la edad

(defrule recomendar-rutina-edad

   ?edad <- (edad ?e)
   ?nivel <- (nivel-condicion-fisica ?n)
   =>
   (if (< ?e 18)
      then
      (printout t "Recomendación de Rutina: Dado que eres muy joven, te recomendamos enfocarte en actividades físicas generales y divertidas como deportes en equipo, natación o actividades al aire libre." crlf)
   else
      (if (<= ?e 30)
         then
         (if (eq ?n "bajo")
            then
            (printout t "Recomendación de Rutina: Para tu edad y nivel de condición física, es importante comenzar con ejercicios cardiovasculares suaves y entrenamiento de fuerza ligero." crlf)
         else if (eq ?n "medio")
            then
            (printout t "Recomendación de Rutina: Puedes realizar una combinación de ejercicios cardiovasculares y de fuerza para mantenerte activo y saludable." crlf)
         else
            (printout t "Recomendación de Rutina: Aprovecha tu nivel de condición física para realizar entrenamientos cardiovasculares y de fuerza con mayor intensidad y variedad." crlf))
      else
         (if (eq ?n "bajo")
            then
            (printout t "Recomendación de Rutina: Enfócate en ejercicios de movilidad, estiramientos y ejercicios suaves para mantener la salud de tus articulaciones y músculos." crlf)
         else if (eq ?n "medio")
            then
            (printout t "Recomendación de Rutina: Realiza una combinación de ejercicios cardiovasculares, de fuerza y flexibilidad para mantener tu condición física y movilidad." crlf)
         else
            (printout t "Recomendación de Rutina: Continúa con ejercicios de fuerza, flexibilidad y actividades aeróbicas para mantener tu bienestar general." crlf)))))



;;;Definir regla para recomendar rutina dependiendo de la genetica y los objetivos

 (defrule recomendar-rutina-genetica-objetivo
   ?genetica <- (tipo-genetica ?g)
   ?objetivo <- (objetivo ?o)
  
   =>
   (if (eq ?o "perder-peso")
      then
      (if (eq ?g "mesomorfo")
         then
         (printout t "Recomendación de Rutina: Para perder peso, una combinación de ejercicios de fuerza y cardio es efectiva. Prueba con levantamiento de pesas, cardio intenso y ejercicios de alta intensidad." crlf)
         else
         (if (eq ?g "ectomorfo")
            then
            (printout t "Recomendación de Rutina: Para perder peso, enfócate en ejercicios cardiovasculares como correr, nadar o ciclismo. También incorpora entrenamiento de fuerza para mantener masa muscular." crlf)
            else
            (printout t "Recomendación de Rutina: Para perder peso, combina ejercicios cardiovasculares con entrenamiento de fuerza. Considera sesiones de cardio moderado y ejercicios de cuerpo completo." crlf)))
      else if (eq ?o "ganar-masa-muscular")
         then
         (if (eq ?g "mesomorfo")
            then
            (printout t "Recomendación de Rutina: Para ganar masa muscular, enfócate en levantamiento de pesas compuesto y ejercicios de fuerza. Dale prioridad a ejercicios de piernas, espalda y pecho." crlf)
            else
            (if (eq ?g "ectomorfo")
               then
               (printout t "Recomendación de Rutina: Para ganar masa muscular, realiza entrenamientos de fuerza intensos y enfócate en levantamiento de pesas. Descansa lo suficiente y consume suficientes calorías." crlf)
               else
               (printout t "Recomendación de Rutina: Para ganar masa muscular, combina ejercicios de fuerza con una dieta adecuada. Prioriza levantamiento de pesas y ejercicios compuestos." crlf)))
      else
         (if (eq ?g "mesomorfo")
            then
            (printout t "Recomendación de Rutina: Para mantener forma, combina ejercicios de fuerza y cardio. Incluye actividades como natación, ciclismo y levantamiento de pesas." crlf)
            else
            (if (eq ?g "ectomorfo")
               then
               (printout t "Recomendación de Rutina: Para mantener forma, realiza ejercicios cardiovasculares regulares y sesiones de entrenamiento de fuerza. Mantén un equilibrio entre ambos tipos de ejercicio." crlf)
               ))))   





;;;Regla para definir deporte segun preferencias

(defrule recomendar-deporte-preferencia
   (preferencia-ejercicio ?preferencia)
   =>
   (printout t "Preferencia de ejercicio ingresada: " ?preferencia crlf)
   (if (eq ?preferencia "cardio")
      then
      (printout t "Recomendación de Deporte: Ejercicio cardiovascular:Si te gusta el ejercicio cardiovascular, podrías considerar actividades como correr, nadar, ciclismo, saltar la cuerda o jugar tenis." crlf)
  
   else if (eq ?preferencia "fuerza")
      then
      (printout t "Recomendación de Deporte: Ejercicios de fuerza: Si prefieres ejercicios de fuerza, podrías disfrutar de levantamiento de pesas, entrenamiento en circuito, yoga o escalada en roca." crlf)


   ))



   ;;;Regla para recomendar alimentacion segun el IMC

(defrule recomendar-alimentacion-imc
   ?imc <- (IMC ?i)
   =>
   (if (< ?i 18.5)
      then
      (printout t "Recomendación de Alimentación: Tu IMC indica que estás en la categoría de bajo peso. Es importante consumir una dieta equilibrada y nutritiva para alcanzar un peso saludable. Considera aumentar el consumo de proteínas magras, grasas saludables y carbohidratos de calidad." crlf)
      else
      (if (< ?i 24.9)
         then
         (printout t "Recomendación de Alimentación: Tu IMC se encuentra en el rango de peso saludable. Mantén una dieta balanceada con una variedad de nutrientes, incluyendo frutas, verduras, proteínas y carbohidratos." crlf)
         else
         (if (< ?i 29.9)
            then
            (printout t "Recomendación de Alimentación: Tu IMC indica que estás en la categoría de sobrepeso. Enfócate en reducir el consumo de alimentos procesados y azúcares añadidos. Incrementa el consumo de verduras, frutas, proteínas magras y granos enteros." crlf)
            else
            (printout t "Recomendación de Alimentación: Tu IMC sugiere que tienes obesidad. Es esencial hablar con un profesional de la salud para crear un plan alimenticio adecuado. En general, prioriza alimentos nutritivos y realiza cambios en tu estilo de vida para mejorar tu salud." crlf)))))






(defrule recomendar-ejercicios-grupo-muscular
   ?enfoque <- (grupo-muscular ?grupo-muscular)
   =>

    (printout t "Preferencia de grupo muscular ingresada:" (lowcase ?grupo-muscular) crlf)
   (if (eq ?grupo-muscular "ninguno")
      then
      (printout t "No has especificado un grupo muscular para enfocar. Si decides enfocarte en algún grupo muscular específico, podré recomendarte ejercicios adecuados." crlf)
      else
      (if (eq (lowcase ?grupo-muscular) "pecho")
         then
         (printout t "Recomendación de Ejercicios para Pecho: Algunos ejercicios efectivos para trabajar el pecho incluyen press de banca, flexiones, press inclinado y aperturas con mancuernas." crlf)
         else if (eq (lowcase ?grupo-muscular) "espalda")
            then
            (printout t "Recomendación de Ejercicios para Espalda: Para trabajar la espalda, puedes realizar ejercicios como dominadas, remo con barra, pulldown y hiperextensiones." crlf)
            else if (eq (lowcase ?grupo-muscular) "brazos")
               then
               (printout t "Recomendación de Ejercicios para Brazos: Trabaja tus brazos con ejercicios como curls de bíceps, extensiones de tríceps, martillo curls y dips." crlf)
               else if (eq (lowcase ?grupo-muscular) "hombros")
                  then
                  (printout t "Recomendación de Ejercicios para Hombros: Ejercicios efectivos para los hombros incluyen press militar, elevaciones lateral
es, elevaciones frontales y pájaros." crlf)
                  else if (eq (lowcase ?grupo-muscular) "muslos")
                     then
                     (printout t "Recomendación de Ejercicios para Muslos: Trabaja tus muslos con ejercicios como sentadillas, estocadas, prensa de piernas y extensiones de cuádriceps." crlf)
                     else if (eq (lowcase ?grupo-muscular) "pantorrillas")
                        then
                        (printout t "Recomendación de Ejercicios para Pantorrillas: Fortalece tus pantorrillas con ejercicios como elevaciones de talones de pie y sentado, y saltos en caja." crlf)
                        else
                        (printout t "No se reconoce el grupo muscular especificado. Por favor, asegúrate de ingresar un grupo muscular válido." crlf))))




    ;;;Definir regla para recomendar ejercicios para la casa si el usuario le gustan

    (defrule recomendar-ejercicios-en-casa-si
   ?lugar-entrenamiento <- (lugar-entrenamiento "si")
   =>
   (printout t "Recomendación de Ejercicios en Casa: Si prefieres entrenar en casa, podrías considerar ejercicios como flexiones, sentadillas, abdominales, burpees, saltos de cuerda, planchas y ejercicios con pesas o bandas de resistencia. Además, puedes explorar rutinas en línea o aplicaciones de entrenamiento en casa." crlf))     