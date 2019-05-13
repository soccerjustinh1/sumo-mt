#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import unittest
import WikiParser
import re

#
# Tests for the verification of parsing input files.
#
class TestWikiParser(unittest.TestCase):

    #
    # Create the Device Under Test (DUT).
    #
    def setup_method(self, method):
        pass

    #
    # Perform any necessary clean-up.
    #
    def teardown_method(self, method):
        pass

    ##############
    # Test-Cases #
    ##############

    def test_invalid_inputfile_none(self):
        self.assertRaises(ValueError, WikiParser.WikiParser, None)

    def test_invalid_inputfile_empty(self):
        self.assertRaises(ValueError, WikiParser.WikiParser, "")

    def test_invalid_inputfile_emptyfile(self):
        self.assertRaises(ValueError, WikiParser.WikiParser, "empty_input.txt")

    def test_valid_inputfile_txt(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        assert self.dut.mInputFilename == expectedFilename

    ##### Now lets test the parsing of some simple lines ###

    def test_template_for_not_fx67(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "\d+\-\d+"

        inputLine = {"originalLine": "{for not fx67}",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1

    def test_template_open_extensions(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "\d+\-\d+"

        inputLine = {"originalLine": "#[[Template:openextensions]]",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1

    def test_hash_star_string(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "\#\*[\s\w]+\."

        inputLine = {"originalLine": "#*This will open a panel where you can manage extension settings.",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1

    def test_double_quotes(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "[\s\w]+\,[\s\w]+\.[\s\w]+\d+\-\d+\s*\,[\s\w]+"

        inputLine = {"originalLine": "Underneath the description of the extension, you will see extension settings. Next to ''Run in Private Windows'', select",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1

    def test_template_table_of_contents(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "\d+\-\d+"

        inputLine = {"originalLine": "__TOC__",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1

    def test_template_button(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "[\s\w]+\{\s*\d+\-\d+\s*\}[\s\w]+\."

        inputLine = {"originalLine": "to add a check mark and then click on the {button Okay, Got It} bar.",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1

    def test_equals_string_equals(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "\d+\-\d+"

        inputLine = {"originalLine": "=Extensions in private windows=",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1

    def test_template_slash_for(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "\d+\-\d+"

        inputLine = {"originalLine": "{/for}",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1

    def test_template_note(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "\d+\-\d+"

        inputLine = {"originalLine": "{note}",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1

    def test_template_slash_note(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "\d+\-\d+"

        inputLine = {"originalLine": "{/note}",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1

    def test_template_triple_quotes(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "\d+\-\d+"

        inputLine = {"originalLine": "'''Note:'''",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1

    def test_link_with_desription(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "\[\[\s+\d+\-\d+\s+\|Firefox\s+version\]\]"

        inputLine = {"originalLine": "[[Find what version of Firefox you are using|Firefox version]]",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1

    def test_image_with_tag(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "\d+\-\d+"

        inputLine = {"originalLine": ";[[Image:Fx67ExtensionInstall-AllowPrivate]]",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1


    def test_brackets_http(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "Mozilla\'s\s*CA\s*Certificate\s*Program\s*publishes\s*a\s*list\s*of\s*\d+\-\d+\s*which\s*contains\s*details\s*that\s*might\s*be\s*useful\s*to\s*the\s*website\s*owners\."

        inputLine = {"originalLine": "Mozilla's CA Certificate Program publishes a list of [https://wiki.mozilla.org/CA/Upcoming_Distrust_Actions upcoming policy actions affecting certificate authorities] which contains details that might be useful to the website owners.",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1

    def test_key_directive(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "\#\s*Press\s*\d+\-\d+\s*\d+\-\d+\s*\+\s*\d+\-\d+\s*\d+\-\d+\s*\."

        inputLine = {"originalLine": "# Press {for mac}{key command}+{/for}{key Delete}.",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1

    def test_filepath_directive(self):

        # Expected outputs.
        expectedRawFilename = "orig_input"
        expectedFilename = expectedRawFilename + ".txt"
        expectedSequence = "\#\s*Press\s*\d+\-\d+\s*\d+\-\d+\s*\+\s*\d+\-\d+\s*\."

        inputLine = {"originalLine": "# Press {for mac}{filepath mypath}+{/for}.",
                     "translatedLine": "",
                     "lineNumber": 99,
                     "sequenceLine": "",
                     "sequences": [],
                     "usedSequenceNumbers": [],
                     "emptyLine": False}

        # Build the Device Under Test.
        self.dut = WikiParser.WikiParser(expectedFilename)

        self.dut.processMediaWikiLine(inputLine)

        currentPattern = re.compile(expectedSequence, re.IGNORECASE)
        currentMatch = re.findall(currentPattern, inputLine["sequenceLine"])

        assert len(currentMatch) == 1


