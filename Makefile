BIN=env/bin/
help:
		@echo "Makefile para a execução do projeto"
		@echo ""
		@echo "Antes de rodar o projeto é recomendado a ultilização da virtualenv rodando o comando: "
		@echo "$ source env/bin/activate"
		@echo ""
		@echo "Como usar: make COMANDO"		
		@echo ""
		@echo "Commandos:"
		@echo "build       Cria executavel do jogo"
		@echo "run         Executa o jogo por linha de comando"
		@echo ""

build:
		$(BIN)pip3 install -r requirements.txt
		$(BIN)pyinstaller main.py -n game --onefile
run:
		$(BIN)pip3 install -r requirements.txt
		$(BIN)python3 main.py