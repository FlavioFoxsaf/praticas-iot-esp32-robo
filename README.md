# Projeto: Robô Explorador Espacial (IoT)

**Instituição:** Universidade SENAI CIMATEC   
**Discentes:** Caio Schneider, Flavio Fox S. A. Fernandes, Henrique Rapadura 

## 🚀 Objetivo da Etapa
Desenvolver e integrar o armazenamento de dados de sensores e a comunicação de um robô explorador físico, utilizando um backend em Python para registrar informações essenciais para a busca de vida extraterrestre.

## 🛠️ Lista de Componentes do Circuito
- ESP32
- 1 Sensor de Temperatura
- 1 Fotorresistor (LDR) para luminosidade
- 1 Sensor de presença (PIR)
- 1 Motor Servo (Movimentação frente/trás)
- 1 LED RGB (Substituindo LEDs verde e vermelho individuais)

## 💻 Instruções de Uso

### Como rodar o backend Python
1. Certifique-se de ter o Python instalado.
2. Abra o terminal e instale o Flask: `pip install flask`
3. Navegue até a pasta `backend` e execute o servidor: `python app.py`

### Como consultar dados salvos
Para visualizar as últimas 100 leituras registradas no banco de dados SQLite, acesse no seu navegador:
`GET http://localhost:5000/leituras`

### Como montar o robô
As instruções detalhadas de pinagem e montagem do hardware com o ESP32, sensores e o Servo Motor serão adicionadas posteriormente na pasta `/firmware`.
