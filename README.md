# 🕹️ Dev de Apps - POO: Grupo 1, Jogo de RPG 🍕

Este projeto visa evidenciar o que aprendemos relacionado ao paradigma de **Orientação a Objetos**, aplicando os conceitos de **Encapsulamento**, **Herança**, **Polimorfismo** e **Classe Principal**.

O programa em si é capaz de simular uma batalha por via de interface **CLI**, solicitando algumas informações inicialmente para respectivamente iniciar a batalha.

É possível assumir o papel (com suas características) de 3 tipos de personagens, sendo Arqueiro, Guerreiro ou Mago.

---

## 🏗️ Arquitetura e Classes do Projeto

### 🧬 Classe Base (`character.py`)

A classe `Character` serve como molde principal (superclasse) para todos os personagens do jogo.

* **Encapsulamento:** Atributos como vida (`__heartPoints`), energia (`__staminaPoints`), ataque (`__attack`), defesa (`__defense`) e nível (`__level`) são privados e acessados de forma controlada via `@property`.
* **Métodos principais:**
  * `attack(other)`: Realiza um ataque básico contra o oponente.
  * `takeDamage(damage)`: Calcula o dano recebido descontando a defesa do personagem (garantindo ao menos `1` de dano caso a defesa seja maior que o ataque).
  * `heal(value)`: Restaura pontos de vida.
  * `levelUp()`: Aumenta o nível e escala os atributos do personagem em 5% (HP/SP) e 10% (Ataque/Defesa).

---

### 🏹 Arqueiro (`arqueiro.py`)

Subclasse de `Character` especializada em ataques à distância, gerenciando sua munição através do atributo privado `__qtdFlecha`.

* **Mecânica exclusiva:** Antes de atacar, verifica se há flechas disponíveis (`atirar()`). Caso a aljava esteja vazia, o jogador pode optar por recarregar novas flechas diretamente pelo terminal.
* **Polimorfismo:** Sobrescreve `attack()` para consumir munição a cada disparo e `__str__()` para exibir a quantidade atual de flechas no status.
* **Métodos auxiliares:** `dar(qtd)` e `tirar(qtd)` para controle da aljava.

### ⚔️ Guerreiro (`guerreiro.py`)

Subclasse de `Character` focada em combate corpo a corpo, com atributos base elevados de ataque e resistência.

* **Polimorfismo:** Sobrescreve `attack()` e `takeDamage()` para exibir mensagens personalizadas de combate com machado durante os turnos.

### 🔮 Mago (`mago.py`)

Subclasse de `Character` que utiliza energia arcana (`_mana`) para potencializar seus feitiços.

* **Mecânica exclusiva:** Possui getter e setter para `mana` e o método `status_mana()`.
* **Polimorfismo:** Sobrescreve `attack()` para consumir `10` pontos de mana e causar `+25` de dano bônus; caso a mana acabe, o feitiço enfraquece e causa apenas `+5` de dano adicional. Também personaliza a mensagem de dano em `takeDamage()`.

---

## ⚔️ Sistema de Batalha e Execução

* **`battle.py`:** Contém a função `battle(char1, char2)`, responsável por gerenciar o loop de turnos. A cada rodada, exibe os status atualizados de ambos os combatentes e alterna os ataques até que os pontos de vida (`getHeartPoints`) de um deles cheguem a zero, declarando o vencedor.
* **`main.py`:** Ponto de entrada da aplicação. Solicita aos dois jogadores a escolha da classe (`1` - Guerreiro, `2` - Arqueiro, `3` - Mago) e o nome de cada personagem por meio da função `choseCharacter()`, instanciando os objetos com seus respectivos atributos iniciais e dando início ao combate.

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3.10+** instalado (necessário devido ao uso da estrutura `match/case`).
2. Clone o repositório e acesse a pasta do projeto:
   ```bash
   git clone <url-do-repositorio>
   cd poo-grupo1-jogo-rpg-main