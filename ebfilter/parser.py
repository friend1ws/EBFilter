#! /usr/bin/env python

from .run import *
import argparse

def create_parser():
    parser = argparse.ArgumentParser(prog = "EBFilter")
    
    parser.add_argument("--version", action = "version", version = "EBFilter-0.2.2")
    
    parser.add_argument("targetMutationFile", metavar = "target.vcf", type = str,
                              help = "the path to the mutation file")
    
    parser.add_argument("targetBamPath", metavar = "target.bam", type = str,
                              help = "the path to the target bam file")
    
    parser.add_argument("controlBamPathList", metavar = "controlBam_list.txt", type = str,
                              help = "the list of paths to control bam files")
    
    parser.add_argument("outputPath", metavar = "output.vcf", type = str,
                              help = "the path to the output")
    
    parser.add_argument('-f', choices=['vcf', 'anno'], default = 'vcf',
                        help = "the format of mutation file vcf or annovar (tsv) format")
    
    parser.add_argument('-t', metavar = "thread_num", default='1', type=int,
                        help = "the number of threads")
    
    parser.add_argument('-q', metavar = "mapping_qual_thres", default='20', type=int,
                        help = "threshold for mapping quality for calculating base counts")
    
    parser.add_argument('-Q', metavar = "base_qual_thres", default='15', type=int,
                        help = "threshold for base quality for calculating base counts")
    
    parser.add_argument('--ff', metavar = "filter_flags", default='UNMAP,SECONDARY,QCFAIL,DUP', type=str,
                        help = "skip reads with mask bits set")
    
    parser.add_argument("--loption", help = "use samtools mpileup -l option", action='store_true', default=False)
    
    parser.add_argument("--region", default = '', type = str,
                        help = "restrict the chromosomal region for mutation. active only if loption is on")
    
    parser.add_argument("--debug", default = False, action = 'store_true', help = "keep intermediate files")
    
    return parser

