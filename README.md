# Email Sender

> Automatización de envío de correos outlook para distintas áreas.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active_Development-orange)

## Overview

Cualquier tarea repetitiva es mejor automatizarla. Usando un template podemos crear un automatizador de envío de correos.

## Arquitectura

El proyecto consta de 3 módulos principales y el main:

* **Módulo de agenda (mail_scheduler):** Su única función es leer desde un archivo .csv los datos que usarémos en el siguiente módulo.
* **Módulo de redacción (mail_maker):** Tras obtener la información usará el template para rellenar los espacios específicados en el template (es importante especificar los campos con los símbolos <>).
* **Módulo de envío (mail_sender):** Ya redactado el email, solo se encargará de enviar el email a los destinatarios y si es necesario realizar copia a cualquier otro destinatario.

## Dependecies

Para este proyecto solo se necesitarán las siguientes dependencias:

    - Python 3
        *Librería de pandas
    - Microsft Outlook
    - Servicio de mensajería POP3



