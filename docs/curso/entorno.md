# Preparar el entorno

Necesitas instalar cinco cosas. Hazlo **antes de la primera sesión**: Android Studio tarda en descargarse.

| Herramienta | Para qué |
|---|---|
| **Node.js 24 LTS** (mínimo 22.22 con Angular 22) y npm | Ejecutar Angular, Ionic y Capacitor |
| **Visual Studio Code** | Editor. Extensiones: *Angular Language Service*, *Ionic*, *ESLint* |
| **Git** y cuenta de **GitHub** (con el correo del IES) | Control de versiones y entregas |
| **Android Studio** (incluye el SDK de Android y Java 21) | Compilar e instalar la app en Android |
| **Google Chrome** | Depurar la app en el navegador y en el móvil (`chrome://inspect`) |

!!! tip "Copia los comandos de uno en uno"
    En esta guía cada comando va en su propio bloque. Pega y ejecuta uno, espera a que termine y pasa al siguiente.

## 1. Instalar según tu sistema

=== "Windows"

    1. Descarga el instalador **LTS** de [nodejs.org](https://nodejs.org) y ejecútalo con las opciones por defecto.
    2. Instala [Git for Windows](https://git-scm.com/download/win). Deja marcada la opción *Git from the command line and also from 3rd-party software*.
    3. Instala [VS Code](https://code.visualstudio.com).
    4. Instala [Android Studio](https://developer.android.com/studio). En el primer arranque elige la instalación **Standard**.
    5. Cierra y vuelve a abrir la terminal (PowerShell) para que reconozca los nuevos comandos.

    Si PowerShell bloquea los scripts de npm, ejecuta esto una vez:

    ```powershell
    Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
    ```

=== "macOS"

    Con [Homebrew](https://brew.sh) instalado:

    ```bash
    brew install node
    ```

    ```bash
    brew install git
    ```

    ```bash
    brew install --cask visual-studio-code
    ```

    ```bash
    brew install --cask android-studio
    ```

    En el primer arranque de Android Studio elige la instalación **Standard**. Si además quieres compilar para iOS necesitas **Xcode** desde la App Store (opcional en este curso).

=== "Ubuntu"

    Instala Node LTS con el repositorio oficial de NodeSource o con `nvm`. Con `nvm`:

    ```bash
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
    ```

    Cierra y abre la terminal, y después:

    ```bash
    nvm install --lts
    ```

    ```bash
    sudo apt install git
    ```

    ```bash
    sudo snap install code --classic
    ```

    ```bash
    sudo snap install android-studio --classic
    ```

    En el primer arranque de Android Studio elige la instalación **Standard**.

## 2. Instalar Ionic CLI

```bash
npm install -g @ionic/cli
```

En macOS o Linux, si da error de permisos, **no uses `sudo`**: instala Node con Homebrew o `nvm` como se indica arriba.

## 3. Comprobar que todo funciona

Ejecuta cada comando. Versiones esperadas: Node **24.x**, Ionic CLI **7.x**.

```bash
node -v
```

```bash
npm -v
```

```bash
git --version
```

```bash
ionic -v
```

## 4. Configurar Android Studio

1. Abre Android Studio → **More Actions → SDK Manager**.
2. En *SDK Platforms* marca la versión de Android más reciente.
3. En *SDK Tools* marca **Android SDK Build-Tools**, **Android SDK Platform-Tools** y **Android Emulator**.
4. (Opcional) En **Device Manager** crea un emulador Pixel reciente.

## 5. Preparar el móvil Android

1. *Ajustes → Información del teléfono* → pulsa 7 veces sobre **Número de compilación**.
2. *Ajustes → Opciones de desarrollador* → activa **Depuración USB**.
3. Conecta el móvil por cable y acepta el aviso *¿Permitir depuración USB?*.
4. En Android Studio, el móvil debe aparecer en la lista de dispositivos.

## 6. Prueba final: tu primera app en el móvil

Crea un proyecto de prueba (acepta las opciones por defecto):

```bash
ionic start prueba blank --type=angular
```

```bash
cd prueba
```

```bash
ionic serve
```

Se abre el navegador con la app. Para verla en el móvil, para el servidor con ++ctrl+c++ y ejecuta:

```bash
ionic build
```

```bash
npx cap add android
```

```bash
npx cap sync android
```

```bash
npx cap open android
```

Se abre Android Studio. Espera a que termine *Gradle sync*, elige tu móvil arriba y pulsa ▶ **Run**.

!!! success "Si ves la app en tu móvil, tu entorno está listo."

Si algo falla, consulta [Problemas frecuentes](../recursos/problemas.md).
