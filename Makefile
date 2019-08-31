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
		@echo "install       Instala requerimentos necessários para rodar o projeto"
		@echo "run         Executa o jogo"
		@echo ""

install:
		virtualenv env
		$(BIN)pip3 install -r requirements.txt
run:
		$(BIN)python3 main.py