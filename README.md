
# 🏰 Masmorra do Fim - RPG Terminal Avançado

<img src="https://github.com/user-attachments/assets/81ad4ed0-d035-43f6-8e2b-0141c829d958" width="230" height="230" alt="Banner do Jogo">

> *"Uma jornada épica através de 14 níveis de desafios, segredos e decisões morais que definem o seu legado."*

---

## 📜 Visão Geral

**Masmorra do Fim** é um RPG de terminal tático, construído em Python, com trilha sonora, escolhas morais, arte ASCII, múltiplos caminhos e finais. Explore o mundo sombrio de **Aldurian**, escolha sua classe, lute por sobrevivência e descubra verdades esquecidas.

---

## 🚀 Funcionalidades Principais

- 🎭 **Sistema de Classes**: escolha entre 5 classes jogáveis com habilidades e atributos únicos  
- 🗺️ **Exploração Multinível**: 14 níveis totalmente distintos com design e narrativa próprios  
- 🧠 **Sistema de Escolhas Morais**: decisões impactam finais, rotas, personagens e conquistas  
- 🏆 **Sistema de Conquistas**: 57 conquistas com feedback visual e notificações (incluindo segredos ocultos)  
- ⚔️ **Sistema de Combate Tático**: baseado em turnos com habilidades especiais e ASCII art  
- 📈 **Progressão por XP**: evolua seu personagem com base em combates e decisões  
- 💀 **Múltiplos Finais**: finais baseados em escolhas, ações e conquistas do jogador  
- 🔊 **Trilha Sonora e Efeitos**: música de fundo e sons temáticos via Pygame  
- 💬 **Narrativa Imersiva**: história dinâmica com eventos, plot twists e NPCs memoráveis  
- 💻 **Interface Estilizada**: menus, transições e diálogos enriquecidos com a biblioteca `rich`  
- ⛓️ **Sistema Modular**: código dividido por níveis, eventos, combate e inventário  
- 🧭 **Sistema de Salvamento Futuro** *(em desenvolvimento para a versão 4.2.0)*

---

## 🆕 Melhorias Recentes (v4.1.0)

- [+] Sistema completo de evolução e distribuição automática de XP  
- [+] Combate 100% redesenhado com controle de fluxo e danos críticos  
- [+] Níveis adicionados:  
  - *O Salão dos Espelhos* (Nível 2)  
  - *A Biblioteca Perdida* (Nível 3)  
  - *O Pântano do Desespero* (Nível 4)  
  - *A Sala do Guardião* (Nível 5)  
  - *O Cárcere das Almas Perdidas* (Nível 6)  
  - *O Abraço das Sombras* (Nível 7)  
- [+] Novos efeitos visuais no terminal com `rich.panel`, `markdown`, e `console`  
- [+] Inclusão do **Monarca das Sombras** como classe desbloqueável com final oculto  
- [+] Implementação de enigmas, diálogos ramificados e armadilhas contextuais

---

## ⚔️ Classes Jogáveis

| Classe                 | Habilidade Especial     | Atributo Forte | Dificuldade |
|------------------------|-------------------------|----------------|-------------|
| 🔮 Mago                | Bola de Fogo            | Magia          | Médio       |
| ⚔️ Guerreiro           | Decapitação             | Força          | Fácil       |
| ✝️ Paladino            | Benção Divina           | Defesa         | Médio       |
| 🏹 Arqueiro            | Tiro Certeiro           | Agilidade      | Difícil     |
| 👑 Monarca das Sombras | Domínio das Sombras     | Corrupção      | Extremo     |

---

## 🏆 Conquistas

Total de **57 conquistas desbloqueáveis**, incluindo segredos ocultos, derrotas perfeitas, interações com NPCs e finais alternativos.

### Destaques:
- 🩸 **"O Impossível Realizado"** – Derrote *Eldramar* em sua forma final  
- 🕊️ **"Libertador de Aldurian"** – Destrua o núcleo corrompido da masmorra  
- 🌑 **"Abraço das Trevas"** – Torne-se o novo Monarca das Sombras  
- 🔍 **"O Leitor Silencioso"** – Descubra todos os segredos da Biblioteca Perdida  
- 💡 **"Inteligência Brilhante"** – Resolva todos os enigmas sem erros

---

## 🧱 Estrutura dos Arquivos

```
Masmorra_fim/
├── main.py                  # Arquivo principal do jogo
├── classes/                 # Lógica das classes jogáveis
├── niveis/                  # Pastas com os 14 níveis do jogo
├── combate/                 # Módulo de batalhas por turno
├── conquistas/              # Sistema de conquistas
├── inventario/              # Gestão de itens e progressão
├── audio/                   # Trilhas sonoras e efeitos
├── utils/                   # Ferramentas auxiliares
└── README.md                # Este documento
```

---

## 📥 Instalação

```bash
# Clone o repositório
git clone https://github.com/CarlosNatanael/Masmorra_fim.git

# Acesse o diretório
cd Masmorra_fim

# Instale as dependências
pip install pygame rich

# Execute o jogo
python main.py
```

> **Requisitos**: Python 3.10+, Pygame 2.0+, Rich 13.0+

---

## 👨‍💻 Desenvolvedores

- **Carlos Natanael** – Dev principal e criador do universo de Aldurian  
- **Arthur Yabuchi** – Tester e consultor de mecânicas e narrativa

---

## 🏁 Versão Atual

```bash
🎮 Masmorra do Fim v4.1.0
```

📅 Última atualização: Maio de 2025  
📘 Próxima versão: **4.2.0** – com sistema de salvamento e final "Ascensão Eterna"

---

## 📜 Licença

Este projeto é de código aberto sob a [MIT License](LICENSE).

---

Pronto para enfrentar os horrores da Masmorra do Fim?

**Escolha seu caminho... e aceite as consequências.**
