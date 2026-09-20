from pathlib import Path
import shutil


CATEGORIAS = {
    ".pdf": "PDFs",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".gif": "Imagens",
    ".doc": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".xls": "Planilhas",
    ".xlsx": "Planilhas",
    ".csv": "Planilhas",
    ".mp3": "Áudios",
    ".wav": "Áudios",
    ".mp4": "Vídeos",
    ".avi": "Vídeos",
    ".zip": "Compactados",
    ".rar": "Compactados"
}


def organizar_arquivos(pasta):
    pasta = Path(pasta)

    if not pasta.exists():
        print("\nA pasta informada não existe.")
        return

    if not pasta.is_dir():
        print("\nO caminho informado não é uma pasta.")
        return

    arquivos = [arquivo for arquivo in pasta.iterdir() if arquivo.is_file()]

    if not arquivos:
        print("\nNenhum arquivo encontrado na pasta.")
        return

    total_organizados = 0

    for arquivo in arquivos:
        extensao = arquivo.suffix.lower()

        if extensao in CATEGORIAS:
            categoria = CATEGORIAS[extensao]
        else:
            categoria = "Outros"

        pasta_destino = pasta / categoria
        pasta_destino.mkdir(exist_ok=True)

        destino = pasta_destino / arquivo.name

        if destino.exists():
            nome_base = arquivo.stem
            extensao_arquivo = arquivo.suffix
            contador = 1

            while destino.exists():
                novo_nome = (
                    f"{nome_base}_{contador}{extensao_arquivo}"
                )
                destino = pasta_destino / novo_nome
                contador += 1

        shutil.move(str(arquivo), str(destino))

        print(
            f"Movido: {arquivo.name} -> {categoria}/"
        )

        total_organizados += 1

    print(
        f"\nOrganização concluída! "
        f"{total_organizados} arquivo(s) organizado(s)."
    )


def main():
    print("===== ORGANIZADOR DE ARQUIVOS =====")
    print("Este programa organiza arquivos por tipo.")

    print("\nExemplo:")
    print(r"C:\Users\jenny\Downloads")

    pasta = input(
        "\nDigite o caminho da pasta que deseja organizar: "
    ).strip()

    organizar_arquivos(pasta)


main()