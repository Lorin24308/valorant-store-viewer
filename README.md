\# Valorant Store Viewer



Projeto desenvolvido para automatizar a coleta da loja diária do VALORANT, realizando a abertura do jogo, navegação até a loja, captura da tela, extração das informações das skins e envio automático via Telegram.



\## 📌 Objetivo



O objetivo do projeto foi criar uma automação completa capaz de:



\- Iniciar o Riot Client

\- Abrir o VALORANT automaticamente

\- Navegar até a loja diária

\- Capturar a tela da loja

\- Extrair nomes e preços das skins utilizando OCR

\- Recortar imagens individuais das armas

\- Enviar os resultados para o Telegram



\## ⚙️ Funcionamento



O fluxo principal do projeto é:



1\. Inicialização do Riot Client

2\. Abertura do VALORANT

3\. Interação automática com a interface (cliques)

4\. Acesso à loja diária

5\. Captura de screenshot

6\. Processamento da imagem

7\. Extração de texto com OCR (Tesseract)

8\. Recorte preciso das skins utilizando coordenadas calibradas

9\. Envio das imagens + informações para o Telegram



\## 🧠 Tecnologias utilizadas



\- Python

\- PyAutoGUI (automação de interface)

\- PyWinAuto (controle de janelas)

\- Pillow (processamento de imagens)

\- Tesseract OCR (extração de texto)

\- Requests (integração com API do Telegram)



\## 🖼️ Processamento de imagem



O projeto utiliza uma abordagem híbrida para captura das skins:



\- Screenshot da tela completa da loja

\- Recorte baseado em coordenadas calibradas manualmente (X/Y)

\- Ajustes finos para centralização das armas

\- Separação das 4 skins diárias em imagens individuais



\## 📲 Integração com Telegram



As skins são enviadas automaticamente utilizando a API do Telegram Bot:



\- Envio de imagem individual por skin

\- Nome da skin + preço (VP) como legenda

\- Possibilidade de expansão para alertas personalizados



\## 🧪 Testes



Foram criados scripts auxiliares para facilitar o desenvolvimento:



\- Captura de coordenadas do mouse

\- Testes de recorte de imagem sem abrir o jogo

\- Validação do OCR isoladamente



\## 🚧 Melhorias futuras



\- Detecção automática da posição das skins (sem coordenadas fixas)

\- Melhoria da precisão do OCR

\- Layout mais elaborado para envio das imagens

\- Execução automática diária (Task Scheduler)

\- Sistema de alerta para skins específicas



\## 📁 Estrutura do projeto

app/

main.py

image\_cropper.py

store\_reader.py

telegram\_sender.py

...

config/

data/





\## 🚀 Como executar



```bash

pip install -r requirements.txt

python -m app.main





\## 🔐 Observação



As credenciais do Telegram (TOKEN e CHAT\_ID) devem ser configuradas localmente e não estão incluídas no repositório por segurança.



Desenvolvido como projeto prático para automação, integração de APIs e processamento de imagens.



