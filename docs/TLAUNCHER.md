# Instalar pelo TLauncher

O TLauncher nao abre arquivos `.mrpack`, entao a instalacao e manual. Peca o arquivo
**`cogs-claws-capes-<versao>-client-files.zip`** para quem cuida do servidor (ele e enviado em particular, nao fica
no GitHub).

> Dica: se puder, use o Freesm Launcher no lugar ([JOGAR-SEM-CONTA.md](JOGAR-SEM-CONTA.md)) - ele importa o modpack
> sozinho e e codigo aberto.

1. **Abra o TLauncher uma vez** e feche o jogo (cria as pastas).
2. **Abra a pasta do jogo:** tecla Windows + R, digite `%appdata%\.minecraft` e Enter.
   - Se ja existe uma pasta `mods` ali com mods de OUTRA versao, renomeie para `mods_antigo`.
3. **Extraia o zip** e copie **tudo** (`mods`, `kubejs`, `versions`, `libraries`) para dentro de `.minecraft`.
   Se perguntar, substitua.
4. No TLauncher: **Configuracoes -> Memoria: 8192 MB** (ou o maximo que der, minimo 6144).
5. Na lista de versoes, escolha **`1.20.1-forge-47.4.10`** (a que voce acabou de copiar). Nao use as versoes com o
   logo do TLauncher para este modpack.
6. **Apelido:** um nome unico (ex.: `Pedro_CCC`). Mande esse nome exato para o dono do servidor te liberar.
7. Clique em **Entrar** (a primeira abertura demora alguns minutos).
8. **Multiplayer -> Adicionar servidor:** `cairo-railroad.tun.ply.gg`
9. Primeira vez no servidor: `/register suasenha suasenha`. Depois: `/login suasenha`.

**Atualizacao do modpack:** apague a pasta `mods` e `kubejs` em `.minecraft` e copie as do zip novo.
