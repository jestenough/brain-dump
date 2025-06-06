import argparse
import subprocess
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Optional
import os

TEX_FILENAME_TEMPLATE: str = "{key}_{lang}.tex"
OUTPUT_DIR_NAME = "dist"


class Language(Enum):
    RUSSIAN = "ru"
    ENGLISH = "en"

    @classmethod
    def list_codes(cls) -> List[str]:
        return [locale.value for locale in cls]


@dataclass(frozen=True)
class ArticleCompileOptions:
    key: str
    languages: List[Language]
    compiler: str


class ArgsHandler:
    @staticmethod
    def valid_folder_key(value: str) -> str:
        folder = Path(value)
        if not folder.exists() or not folder.is_dir():
            raise argparse.ArgumentTypeError(f"Folder '{value}' does not exist or is not a directory")
        return value

    @staticmethod
    def valid_language(value: str) -> str:
        if value not in Language.list_codes():
            raise argparse.ArgumentTypeError(f"Unsupported language: {value}")
        return value

    @classmethod
    def parse_args(cls) -> argparse.Namespace:
        parser = argparse.ArgumentParser(description="Compile LaTeX articles by key and languages")
        parser.add_argument(
            "-k", "--key",
            type=cls.valid_folder_key,
            required=True,
            help="Folder with LaTeX files (article key)"
        )
        parser.add_argument(
            "-l", "--languages",
            nargs="+",
            type=cls.valid_language,
            default=Language.list_codes(),
            help="Languages for compilation (default: all)"
        )
        return parser.parse_args()


class LatexCompiler:
    def __init__(self, options: ArticleCompileOptions):
        self.options = options

    def get_tex_file_path(self, lang: Language) -> Optional[Path]:
        filename = TEX_FILENAME_TEMPLATE.format(key=self.options.key, lang=lang.value)
        tex_file = Path(self.options.key) / filename
        if not tex_file.exists():
            print(f"File for language '{lang.value}' not found: {tex_file}")
            return None
        return tex_file

    def compile(self, lang: Language) -> bool:
        tex_file_path = self.get_tex_file_path(lang)
        if not tex_file_path:
            return False

        print(f"Compiling {tex_file_path}...")

        output_dir_path = Path('.') / OUTPUT_DIR_NAME
        output_dir_path.mkdir(parents=False, exist_ok=True)

        try:
            for _ in range(2):
                result = subprocess.run(
                    [
                        self.options.compiler,
                        "-interaction=nonstopmode",
                        f"-output-directory={output_dir_path}",
                        str(tex_file_path)
                    ],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                if result.returncode != 0:
                    print(f"Compilation error for {tex_file_path}:\n{result.stdout}\n{result.stderr}")
                    return False
            print(f"Successfully compiled: {tex_file_path.with_suffix('.pdf')} to ./{output_dir_path} folder")
            return True
        except Exception as e:
            print(f"Exception during compilation of {tex_file_path}: {e}")
            return False

    def compile_all(self) -> None:
        for lang in self.options.languages:
            self.compile(lang)


if __name__ == "__main__":
    args = ArgsHandler.parse_args()
    selected_languages = [Language(lang) for lang in args.languages]
    options = ArticleCompileOptions(key=args.key, languages=selected_languages, compiler="pdflatex")
    compiler = LatexCompiler(options)
    compiler.compile_all()
