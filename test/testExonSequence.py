#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:13:24 2018

@author: beccalove
"""

import unittest
import veffects

class ExonSequenceForwardTestCase(unittest.TestCase):
    
    def setUp(self):
        
        self.exon = veffects.ExonSequence("2L", "foo", 3, "+", 109, 134)
        self.test_seq = "CGATATGAATATGACCAGATATGAGT"
        
    def test_length(self):
        
        self.assertEqual(self.exon.length, 26)
        
    def test_add_sequence(self):
        
        self.exon.add_sequence(self.test_seq)
        
        self.assertEqual(self.exon.sequence, self.test_seq)
        
    def test_sequence_is_right_length(self):
        
        test_seq = "A"

        self.assertRaises(ValueError, self.exon.add_sequence, test_seq)
    
    def test_change(self):
        
        self.exon.add_sequence(self.test_seq)
        
        variant1 = veffects.VariantRecord("2L", 110, "GA", "G")
        variant2 = veffects.VariantRecord("2L", 118, "T", "C")
        variant3 = veffects.VariantRecord("2L", 125, "A", "AAAAAAA")
        variant4 = veffects.VariantRecord("2L", 131, "GAG", "G")
        
        variants = [variant1, variant2, variant3, variant4]
        
        self.exon.variants = variants
        
        test_changed_seq = "CGTATGAACATGACCAAAAAAAGATATGT"
        
        self.exon.change()
        
        self.assertEqual(self.exon.changed_sequence, test_changed_seq)
        
    def test_change_ref_alleles_mismatch(self):
        
        self.exon.add_sequence(self.test_seq)
        
        variant1 = veffects.VariantRecord("2L", 131, "GGG", "G")
        
        self.assertRaises(ValueError, self.exon.add_sequence, [variant1])
    
    def test_change_allele_out_of_bounds(self):
        
        self.exon.add_sequence(self.test_seq)
        
        variant1 = veffects.VariantRecord("2L", 4, "G","GGGG")
        
        self.assertRaises(ValueError, self.exon.add_sequence, [variant1])
       
    def test_change_chroms_mismatch(self):
        
        self.exon.add_sequence(self.test_seq)
        
        variant1 = veffects.VariantRecord("2L", 118, "T", "C")
        variant2 = veffects.VariantRecord("3L", 118, "T", "C")
        
        variants = [variant1, variant2]
        
        self.assertRaises(ValueError, self.exon.add_sequence, variants)

'''        
class ExonSequenceReverseTestCase(unittest.TestCase):
    
    def setUp(self):
        
        self.exon = veffects.ExonSequence("3R", "bar", 2, "-", 10, 34)
        self.test_seq = "TTGTCGTGTACATGGTACTAGCTA"
        
    def test_length(self):
        
        self.assertEqual(self.exon.length, 24)
        
    def test_add_sequence(self):
        
        self.exon.add_sequence(self.test_seq)
        
        self.assertEqual(self.exon.sequence, self.test_seq)
    
    def test_change(self):
        
        self.exon.add_sequence(self.test_seq)
        
        variant1 = veffects.VariantRecord("3R", 11, "A", "AAA")
        variant2 = veffects.VariantRecord("3R", 14, "ACG", "A")
        variant3 = veffects.VariantRecord("3R", 125, "A", "AAAAAAA")
        variant4 = veffects.VariantRecord("3R", 131, "GAG", "G")
        
        variants = [variant1, variant2, variant3, variant4]
        
        self.exon.variants = variants
        
        test_changed_seq = "CGTATGAACATGACCAAAAAAAGATATGT"
        
        self.exon.change()
        
        self.assertEqual(self.exon.changed_sequence, test_changed_seq)
        
    def test_change_ref_alleles_mismatch(self):
        
        self.exon.add_sequence(self.test_seq)
        
        variant1 = veffects.VariantRecord("2L", 131, "GGG", "G")
        
        self.assertRaises(ValueError, self.exon.add_sequence, [variant1])
    
    def test_change_allele_out_of_bounds(self):
        
        self.exon.add_sequence(self.test_seq)
        
        variant1 = veffects.VariantRecord("2L", 4, "G","GGGG")
        
        self.assertRaises(ValueError, self.exon.add_sequence, [variant1])
       
    def test_change_chroms_mismatch(self):
        
        self.exon.add_sequence(self.test_seq)
        
        variant1 = veffects.VariantRecord("2L", 118, "T", "C")
        variant2 = veffects.VariantRecord("3L", 118, "T", "C")
        
        variants = [variant1, variant2]
        
        self.assertRaises(ValueError, self.exon.add_sequence, variants)'''