# Teclas de heroi (opcional)

Quem quiser o mesmo layout de teclas do dono do servidor: importe o arquivo **`cogs-claws-capes-<versao>-hero-keys.mrpack`**
da pagina de releases em vez do normal. Tudo de heroi fica na mao esquerda:

| Tecla | Acao |
|---|---|
| **Shift** (segurar) | correr |
| **Ctrl** | agachar |
| **Z X C V B** | poderes 1 a 5 do traje |
| **G** | proxima pagina de poderes |
| **R** | Iron Man: sistema de armas |
| **H** | Iron Man: travar alvo |
| **Y** | Iron Man: escudo |
| **'** (tecla do canto esquerdo, acima do Tab) | Iron Man: esfriar (heat) |
| **J** | Iron Man: modular |
| **O** | abrir mochila |
| **I** | menu Curios (acessorios) |
| teclado numerico **+ - \* 0 1 2 3 4** | waypoint novo, config. do minimapa, ampliar mapa, jetpack on/off, upgrades da mochila 1 e 2, terminal Tom's, painel CoreWithStuff |

Teclas que continuam repetidas (Armadura do Cataclysm, aljava, livro de feiticos, montar dragao) so funcionam
segurando ou vestindo o item delas, entao nao atrapalham os poderes.

Ja tem a instancia e quer trocar sem reinstalar? Peca para o dono do servidor, ou mude em
Opcoes -> Controles -> Atribuicoes de teclas.

Para o dono do servidor (botao no HUD ou terminal, com o jogo FECHADO):
`python tools\fix_keybinds.py --hold-sprint` aplica o layout (faz backup) e `--restore` volta ao anterior.
