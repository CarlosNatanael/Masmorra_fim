# 🏰 Masmorra do Fim - RPG Terminal Avançado

<img src="https://github.com/user-attachments/assets/81ad4ed0-d035-43f6-8e2b-0141c829d958" width="230" height="230" alt="Banner do Jogo">

*"Uma jornada épica através de 14 níveis de desafios mortais e escolhas impactantes"*

---

## 📜 Visão Geral
**Masmorra do Fim** é um RPG narrativo e estratégico que roda diretamente no terminal. Cada decisão pode salvar ou condenar o jogador no mundo sombrio de Aldurian. Com:

- 🔗 14 níveis interconectados com múltiplos finais
- 🧙‍♂️ 5 classes jogáveis com habilidades únicas
- 🏆 57 conquistas com sistema de notificações
- 🖼️ Combate em ASCII art dinâmico
- 🎵 Trilha sonora e efeitos sonoros imersivos
- 🎮 Sistema de experiência e evolução de personagem

---

## 📂 Formas de Jogar

### 🔹 1. Modo Tradicional (Python)
Requisitos:
- Python 3.10+
- Bibliotecas: `pygame`, `rich`, `plyer`

```bash
# Clone o repositório
git clone https://github.com/CarlosNatanael/Masmorra_fim.git
cd Masmorra_fim

# Instale as dependências
pip install -r requirements.txt

# Inicie o jogo
python main.py
```

### 🔹 2. Modo Simples (Executável)
Para quem **não quer instalar Python ou bibliotecas**, há uma versão **executável (.exe)** disponível para Windows:

> ✅ Basta baixar o arquivo `Masmorra_do_Fim.exe`, clicar duas vezes e jogar!

📥 Acesse a aba [Releases](https://github.com/CarlosNatanael/Masmorra_fim/releases) para baixar a última versão.

---

## ⚔️ Classes Disponíveis

| Classe                | Habilidade Especial     | Dificuldade |
|-----------------------|-------------------------|-------------|
| 🔮 Mago               | Bola de Fogo            | Médio       |
| ⚔️ Guerreiro         | Decapitação             | Fácil       |
| ✝️ Paladino          | Benção Divina           | Médio       |
| 🏹 Arqueiro          | Tiro Certeiro           | Difícil     |
| 👑 Monarca das Sombras | Domínio das Sombras   | Extremo     |

---

## 🏆 Conquistas Notáveis

- **"O Impossível Realizado"** – Derrote Eldramar em sua forma final
- **"Libertador de Aldurian"** – Destrua o núcleo da masmorra
- **"Abraço das Trevas"** – Torne-se o novo Monarca

No total, são **57 conquistas**, incluindo segredos ocultos e interações especiais.

---

## 🛠️ Tecnologias Utilizadas

- ![Python](https://img.shields.io/badge/Python-3.10+-yellow?logo=python)
- ![Pygame](https://img.shields.io/badge/Pygame-2.0+-blue?logo=pygame)
- ![Rich](https://img.shields.io/badge/Rich_Terminal-13.0+-orange)
- Sistema de conquistas com notificações desktop (`plyer`)

---

## 📦 Estrutura do Projeto

```
Masmorra_Fim/
│
├── utils/
│	│
│	├── combate.py		            # Sistema de combate
│	├── personagem.py               # Escolha da classe e atributos do personagem
│	├── creditos.py	                # Créditos do final do jogo
│	└──	utils.py                    # Funções auxiliares
├── models/
│	│
│	├── nivel1.py                
│	├── nivel2.py               
│	├── nivel3.py                
│	├── nivel4.py               
│	├── nivel5.py                
│	├── nivel6_1.py             
│	├── nivel6_2.py              
│	├── nivel6_3.py			   
│	├── nivel7_h.py              
│	├── nivel7_s.py              
│	├── nivel8.py	
│	├── nivel9.py              
│	├── nivel9_s.py  		     
│ └── nivel10.py
├── conquistas_imag/
│   |
│   ├── conquista.py
│   ├── sistema_conquista.py
│   ├── anotaçãoes conquistas.txt
│   ├── __init__.py
│   └── # imagens das conquistas.png
├── sound/
│   |
│   └── # Todos as musicas dos cápitulos
├── game_sound_py/
│   |
│   ├── game-over.py
│   ├── menu_sound.py
│   ├── sound1.py
│   ├── sound2.py
│   ├── sound3.py
│   ├── sound4.py
│   ├── sound5.py
│   ├── sound6.py
│   ├── sound7.py
│   ├── sound8.py
│   ├── sound9.py
│   └── sound10.py
├── main.py                  
├── icone.ico			    
├── README.md
├── .gitignore
├── masmorra.spec
├── version.txt
└── LICENSE
```

---

## 👨‍💻 Créditos

**Desenvolvido por:** Carlos Natanael  
**Testes e feedback:** Arthur Yabuchi

```bash
Versão Atual: 4.1.0
```

---

> 🎮 *"Você sobreviverá à masmorra... ou se tornará parte dela?"*
