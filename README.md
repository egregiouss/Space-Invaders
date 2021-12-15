# Space-Invaders
Space invaders on Python.

## Usage

```sh
python3 main.py
```
*GUI

*Корректная механика игры

*Несколько уровней

*Начисление очков

*Таблица рекордов

*Несколько жизней

*Бункеры

*Mystery ship

## Build
Build via pyinstaller
1) Install pyinstaller via pip:
   ```sh
  pip install pyinstaller
  ```
2) run pyinstaller:
 ```sh
pyinstaller --noconfirm --onedir --windowed --add-data "<absolute path to folder 'game'>;game/"  "<absolute path to main.py"
```
3) from folder 'output' run main.exe

