# import things here to make them visible to Plone.
# Note, just commenting something out here isn't enough--
# the Install.py method also should be changed,
# and the __init__ method for HelpCenter.py.

from . import HelpCenter

from . import FAQFolder, FAQ

from . import HowToFolder, HowTo

from . import TutorialFolder, Tutorial, TutorialPage

from . import ReferenceManualFolder, ReferenceManual, ReferenceManualSection, ReferenceManualPage

from . import InstructionalVideoFolder, InstructionalVideo

from . import LinkFolder, Link

from . import ErrorReferenceFolder, ErrorReference

from . import Glossary, Definition

from . import KnowledgeBase, LeafPage
