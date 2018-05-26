# coding: utf8
from __future__ import unicode_literals

import conll2json
from pathlib import Path
import plac

from spacy.cli._messages import Messages
from spacy.util import prints

input_path = Path('id_gsd-ud-train.conllu')
output_path = Path('data')
if not input_path.exists():
    prints(input_path, title=Messages.M028, exits=1)
if not output_path.exists():
    prints(output_path, title=Messages.M029, exits=1)
conll2json.conllu2json(input_path, output_path, n_sents=4477, use_morphology=False)