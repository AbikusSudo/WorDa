# WorDa — продвинутый VPN-клиент для Android
## Создатель: AbikusSudo
### Проект: https://github.com/AbikusSudo/WorDa
[![API 21+](https://badgen.net/badge/Android/21+/brightgreen)](https://developer.android.com/about/versions/android-5.0)
[![Лицензия GPL-3.0](https://badgen.net/badge/license/GPL--3.0/orange)](https://www.gnu.org/licenses/gpl-3.0)
[![Статус сборки](https://badgen.net/github/checks/AbikusSudo/WorDa/main)](https://github.com/AbikusSudo/WorDa/actions)
[![Telegram-канал](https://badgen.net/badge/Telegram/новости/33A6E8)](https://t.me/ItsWorDa)

WorDa — это универсальный клиент для защищённого подключения к интернету. Он построен на собственной платформе с акцентом на поддержку современных протоколов, а также предоставляет расширенные функции, такие как правила маршрутизации, полную статистику и удобный тёмный интерфейс.

> **Осторожно, сторонние сборки!**
> Официальная версия приложения распространяется только через [GitHub Releases!](https://github.com/AbikusSudo/WorDa/releases) Версии из Google Play или других магазинов **не являются официальными** и могут содержать нежелательные изменения. Безопасность и корректность их работы не гарантируются! Надеюсь вы услышали.

---

## 📥 Установка и обновление

### Рекомендуемый способ (GitHub Releases)
1.  Перейдите на страницу **[последнего релиза](https://github.com/AbikusSudo/WorDa/releases)**.
2.  Скачайте файл с расширением **`.apk`** (например, `WorDa-v1.2.3-release.apk`).
3.  На Android-устройстве откройте скачанный файл и разрешите установку из неизвестных источников при запросе системы.

### Для разработчиков и тестировщиков
-   **Сборка из исходников:** Инструкция приведена в разделе [🧑‍💻 Для разработчиков](#-для-разработчиков).

---

## 🌐 Поддерживаемые протоколы и функции

### Основные протоколы
WorDa поддерживает широкий спектр протоколов для различных сценариев:
Если не грузит, используйте (эту)[http://cdn-0.plantuml.com/plantuml/png/PLLDJnDT6DttLzmbBwy6CN5FWaODVX2duj9Cw4H6sXaoRKFSqVAT4X1rOKmKr8qRasbXxCUqy1Vk_KUUvypSja4DuNxSUvvpddFki52jkL6juWUbYhjHgAxxmOORkHLL2ODmTIqAAvwgHNLlQkT5M0zAYs4KU96QlrCepAfNONJVLIlBpvJ-ebFTquaUcMPXTbRfCtsbB_4_CLlw3tOwEiRkqBHqelGr5gzC4qS6-4bD2rTmvpic7MpXd2012wVdz3acE9SlNffj2oItGCAFl8TrDoeL_iU_rqf_C2tJ87PiJXI6kCo23TCqH_RKFyKmJvGvq3sp8wV9U2IQnZTC4qjjBANc25iMK4XGVuo51kxlwuHLUvQYi-QMmirgkBfUpHPMddfLEtpom76oOJ4Atxg1BVSBI5jJCaW9NAKge8UsFhOKHjlcCD_hO7miCzrNE3YYdfY7jz2y0Nvl4xblstwDctiu6jF4BWlR1j24dD_BnulPwD6xQisBV5VDpzsrVB_1LXAx0G40XI2a404uKfnk8ypQ5NK9bi7Oelq6wnqndfWTeZ0tFGM1rc1em2gpXA0nMi0U40pLCtsdMEhATAB4URwuvDpBjHIBopFEVxRmJvhU4JmKYJEIj03Oqvc6BuNSURGRdcS5G0_7kk8F3Z4b8Y6ZyX7GxTnHd8XHuq1CeSWkvd01MpFEHjclgM8z2Boo7xmPa_jgVHJbWfFtHAUibf1xtxPRR4SvT0VD4uQCUvSFbdTwIgG9X3dHGucDq6GPlBDJ88hxm8l5IHRgsoKHEyYbn_GEdL8pItwvh9nDlxQwDcPzIde3cmdofeWO5lUcP6ICkw3J4WU4w6qwdK0Haao1Q905FgEWI_hV8TvXTWHtsTI4lWpG49jbivj9_CICJDkR1LESu8Yynja6tGPK9FPRPelSK04BcUNyGt1y2vM5aJd2A7kx9sOlO_0P2qWKn3OLepmYpWKV9vCmUGrdDvCdQ2FntBvvBE4wq1Whfjy6zbeKYG4MxHmbzlCFddHFjsbmEkbTWvNu22Rlw0SICRJD4iDHQVnSUVk2pxrf8zBZ11XyoNtJG1FQMGefyv1XnQrKN9-0lH-_-kaFKKmzy9LFAuK2ke3CBdX1AVz3zXS0] сыллку.
!(Поддерживаемые протоколы и функции)[http://cdn-0.plantuml.com/plantuml/png/PLLDJnDT6DttLzmbBwy6CN5FWaODVX2duj9Cw4H6sXaoRKFSqVAT4X1rOKmKr8qRasbXxCUqy1Vk_KUUvypSja4DuNxSUvvpddFki52jkL6juWUbYhjHgAxxmOORkHLL2ODmTIqAAvwgHNLlQkT5M0zAYs4KU96QlrCepAfNONJVLIlBpvJ-ebFTquaUcMPXTbRfCtsbB_4_CLlw3tOwEiRkqBHqelGr5gzC4qS6-4bD2rTmvpic7MpXd2012wVdz3acE9SlNffj2oItGCAFl8TrDoeL_iU_rqf_C2tJ87PiJXI6kCo23TCqH_RKFyKmJvGvq3sp8wV9U2IQnZTC4qjjBANc25iMK4XGVuo51kxlwuHLUvQYi-QMmirgkBfUpHPMddfLEtpom76oOJ4Atxg1BVSBI5jJCaW9NAKge8UsFhOKHjlcCD_hO7miCzrNE3YYdfY7jz2y0Nvl4xblstwDctiu6jF4BWlR1j24dD_BnulPwD6xQisBV5VDpzsrVB_1LXAx0G40XI2a404uKfnk8ypQ5NK9bi7Oelq6wnqndfWTeZ0tFGM1rc1em2gpXA0nMi0U40pLCtsdMEhATAB4URwuvDpBjHIBopFEVxRmJvhU4JmKYJEIj03Oqvc6BuNSURGRdcS5G0_7kk8F3Z4b8Y6ZyX7GxTnHd8XHuq1CeSWkvd01MpFEHjclgM8z2Boo7xmPa_jgVHJbWfFtHAUibf1xtxPRR4SvT0VD4uQCUvSFbdTwIgG9X3dHGucDq6GPlBDJ88hxm8l5IHRgsoKHEyYbn_GEdL8pItwvh9nDlxQwDcPzIde3cmdofeWO5lUcP6ICkw3J4WU4w6qwdK0Haao1Q905FgEWI_hV8TvXTWHtsTI4lWpG49jbivj9_CICJDkR1LESu8Yynja6tGPK9FPRPelSK04BcUNyGt1y2vM5aJd2A7kx9sOlO_0P2qWKn3OLepmYpWKV9vCmUGrdDvCdQ2FntBvvBE4wq1Whfjy6zbeKYG4MxHmbzlCFddHFjsbmEkbTWvNu22Rlw0SICRJD4iDHQVnSUVk2pxrf8zBZ11XyoNtJG1FQMGefyv1XnQrKN9-0lH-_-kaFKKmzy9LFAuK2ke3CBdX1AVz3zXS0]

---

## ⚙️ Начало работы

### 1. Добавление сервера
1.  Откройте приложение и нажмите "Добавить конфигурацию" (+).
2.  Выберите способ:
    -   **Сканировать QR-код** (самый быстрый).
    -   **Импортировать ссылку-подписку** (URL).
    -   **Ввести параметры вручную**.
3.  Для протоколов Exclave/Happ укажите ключ, адрес сервера и порт, предоставленные вашим провайдером.

### 2. Настройка маршрутизации (Split Tunneling)
1.  В списке конфигураций нажмите и удерживайте нужную, затем выберите "Редактировать".
2.  Перейдите в раздел **"Правила приложений"**.
3.  Для каждого приложения выберите "Обход VPN" (трафик идёт напрямую) или "Блокировка" (трафик полностью заблокирован).

### 3. Включение аварийного выключателя (Kill Switch)
-   Перейдите в **Настройки** → **Безопасность**.
-   Активируйте переключатель **"Аварийный выключатель"**.
-   Рекомендуется включать эту функцию для максимальной защиты конфиденциальности.

---

## ❗ Частые проблемы и их решение
Если не грузит, используйте (эту)[http://www.plantuml.com/plantuml/png/ZLHBZjD05Dpx56y98t61MSq6SG2GM9k91HQn4pa9ccMSe04fA4QpvuEuG9E99qwSpnLUNu6JKALs1v1YAPl4_VogNhtgagy6mp0R9d7QIS9-C7WRf_qm2nD9Ucdl-atMIo8PPgCe22v4lzcnxlMNrbhgriv4Aq6bj1zntcbbY-02NLzGcOWUqBhKZTPsRZ_yqz3mL2XMA9fB8K8NG8rvjeK0jTUTVO-6Upj5sTXRZmRy-z-HMbvwMIGWxSH-4Z-M0dFMcxUcXU67Rddow0C9xGIa55BBewStrztmNII_R-_aPPn5pqPXrdbyjfpd_Muyb1UZD8swSVgQBkcTdTcS4u1Q2xNfoevjeKk1mmRJ3RtLwhHbdtM3bWfZd6Ka06vFdEX2O1uirB95urVqUO-SHWUWS3W-5x0T1u0rPy_P-_AsICyGi5gU2eEkVLe4XorRx9WZyJjbX32qy34we9m3Rze3v1gNoe4FIk76nHJsSZcKj_Jr_10jcyMdu3wQ8FZBGLhpvbhZnDnGi-CqZc_1pQ1wvnpUq6CP811FNlLk_WjzS5nIQrGVFBVeYY3mp4ZhNMernQ-WngMPTXfuKj3dDYEQA-EaUohMbR_MARcuawxv10dx5fAVRgeBbFVpG35QKnOMdSC3vpUAbPq7Lr7QQRv3Vm00] сыллку
![Диаграмма проблем и решений для WorDa](http://www.plantuml.com/plantuml/png/ZLHBZjD05Dpx56y98t61MSq6SG2GM9k91HQn4pa9ccMSe04fA4QpvuEuG9E99qwSpnLUNu6JKALs1v1YAPl4_VogNhtgagy6mp0R9d7QIS9-C7WRf_qm2nD9Ucdl-atMIo8PPgCe22v4lzcnxlMNrbhgriv4Aq6bj1zntcbbY-02NLzGcOWUqBhKZTPsRZ_yqz3mL2XMA9fB8K8NG8rvjeK0jTUTVO-6Upj5sTXRZmRy-z-HMbvwMIGWxSH-4Z-M0dFMcxUcXU67Rddow0C9xGIa55BBewStrztmNII_R-_aPPn5pqPXrdbyjfpd_Muyb1UZD8swSVgQBkcTdTcS4u1Q2xNfoevjeKk1mmRJ3RtLwhHbdtM3bWfZd6Ka06vFdEX2O1uirB95urVqUO-SHWUWS3W-5x0T1u0rPy_P-_AsICyGi5gU2eEkVLe4XorRx9WZyJjbX32qy34we9m3Rze3v1gNoe4FIk76nHJsSZcKj_Jr_10jcyMdu3wQ8FZBGLhpvbhZnDnGi-CqZc_1pQ1wvnpUq6CP811FNlLk_WjzS5nIQrGVFBVeYY3mp4ZhNMernQ-WngMPTXfuKj3dDYEQA-EaUohMbR_MARcuawxv10dx5fAVRgeBbFVpG35QKnOMdSC3vpUAbPq7Lr7QQRv3Vm00)

---

## 🧑‍💻 Для разработчиков

### Сборка проекта
1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/AbikusSudo/WorDa.git
    cd WorDa
    ```
2.  **Откройте проект в Android Studio** (рекомендуется Arctic Fox или новее).
3.  **Синхронизируйте зависимости Gradle** (файл `build.gradle.kts`).
4.  **Соберите APK** через меню `Build` → `Build Bundle(s) / APK(s)` → `Build APK(s)`.

### Архитектура и вклад в проект
Проект использует современный стек Android (Kotlin, Coroutines, Jetpack Compose) и модульную архитектуру. Основные модули:
-   `:app` — точка входа и UI-слой.
-   `:core` — бизнес-логика, управление подключениями.
-   `:protocols` — реализации протоколов (Exclave, Happ, WireGuard и др.).
-   `:tunnel` — низкоуровневое управление туннелями и правилами.

Мы приветствуем пул-реквесты! Перед тем как начать работу над новой функцией, обсудите её в [Issues](https://github.com/AbikusSudo/WorDa/issues)!

---

## 📄 Лицензия и контакты

-   **Лицензия:** Этот проект распространяется под лицензией [GNU GPL v3.0](https://github.com/AbikusSudo/WorDa/blob/main/LICENSE). Вы можете свободно использовать, изменять и распространять код с соблюдением условий лицензии.
-   **Официальный сайт:** [https://worda.2bd.net](https://worda.2bd.net)
