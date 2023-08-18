# Sistema de recomendación de restaurantes

Sistema que utiliza el filtrado colaborativo y la similitud por coseno para recomendar restaurantes a usuarios que cuenten con al menos una
reseña en Google Maps o Yelp.

## Tecnologías Utilizadas

| ![Imagen 1](https://github.com/hernandroz/testeo13ago2023/blob/main/imagenes_readme/Python-logo-notext.png) | ![Imagen 2](https://github.com/hernandroz/testeo13ago2023/blob/main/imagenes_readme/Visual_Studio_Code_1.35_icon.svg.png) | ![Imagen 3](https://github.com/hernandroz/testeo13ago2023/blob/main/imagenes_readme/Pandas_logo.svg.png) | ![Imagen 4](https://github.com/hernandroz/testeo13ago2023/blob/main/imagenes_readme/2560px-Scikit_learn_logo_small.svg.png) 
|:-----------------------:|:-----------------------:|:-----------------------:|:-----------------------:|
|    Python        |    Visual Studio Code        |    Pandas        |    Scikit-learn        

| ![Imagen 4](https://github.com/hernandroz/testeo13ago2023/blob/main/imagenes_readme/uvicorn.png) | ![Imagen 5](https://github.com/hernandroz/testeo13ago2023/blob/main/imagenes_readme/1_UQpQJjVtSuUFxXmb64hqYw.png) | ![Imagen 6](https://github.com/hernandroz/testeo13ago2023/blob/main/imagenes_readme/MRd3wYu7.png) | ![Imagen 7](https://github.com/hernandroz/testeo13ago2023/blob/main/imagenes_readme/image27_frqkzv.png) |
|:-----------------------:|:-----------------------:|:-----------------------:|:-----------------------:|
|    Uvicorn        |    FastAPI        |    render.com        |    streamlit        


## Uso

Cualquier persona puede acceder a nuestro sistema de recomendación mediante el siguiente link: [Streamlit](https://streamlit.io/).
Se deberá ingresar un id de usuario y el sistema retornará recomendación de restaurantes cercanos al usuario.

## Estructura del Proyecto

El algoritmo de recomendación se desarrolló utilizando el lenguaje de programación Python, y consta de la siguiente estructura:

-1. Eliminación de reviews del mismo usuario: Transformaremos nuestro dataset para quedarnos con una sola review única por cada usuario.
Si un usuario tiene registradas más de 1 review, solo se considerará la efectuada más recientemente y las demás se eliminaran.

Proporciona una descripción general de la estructura de tu proyecto, incluyendo directorios y archivos clave.

## Ejemplos

Ofrece ejemplos de código o capturas de pantalla que muestren cómo utilizar tu proyecto en diferentes situaciones.

## Contribuciones

Si aceptas contribuciones, describe cómo los colaboradores pueden participar. Incluye pautas para informar problemas y enviar solicitudes de extracción.

## Licencia

Indica bajo qué licencia se distribuye tu proyecto.

## Créditos

Agradece a bibliotecas, recursos y fuentes de datos que hayas utilizado en tu proyecto, así como a los autores de las tecnologías clave.

## Contacto

Proporciona información de contacto para ti o tu equipo.

## Agradecimientos

Agradece a las personas o recursos que te han ayudado en el desarrollo del proyecto.

