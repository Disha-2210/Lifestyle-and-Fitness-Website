#!/usr/bin/env perl
use strict;
use warnings;

use File::Copy;

my $source_dir = "/home/Desktop/file";
my $target_dir = "/home/Desktop/Perl_script";

opendir(my $DIR, $source_dir) || die "can't opendir $source_dir: $!";  
my @files = readdir($DIR);

foreach my $t (@files) {
  if (-f "$source_dir/$t" ) {
    # Check with -f only for files (no directories)
    copy "$source_dir/$t", "$target_dir/$t";
  }
}

closedir($DIR);