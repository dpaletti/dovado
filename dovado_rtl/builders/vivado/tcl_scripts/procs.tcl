proc create_file_list { dir} {
    set contents [glob -nocomplain -directory $dir *]
    set subdirs {}
    set files {}
    foreach item $contents {
        if { [file isdirectory $item] } {
            lappend subdirs $item
        } else {
            lappend files $item
        }
    }

    foreach item $subdirs {
        set contents [glob -nocomplain -directory $item *]
        foreach iitem $contents {
            lappend files $iitem
        }
    }
    
    return $files
}

proc get_depth string {
    regexp -all / $string
}

proc read_all_files { dir libs} {
    set filenames [create_file_list $dir]
    set depths [lmap f $filenames {get_depth $f}]
    set indices [lsort -indices -integer -decreasing $depths]
    set filenames [lmap idx $indices {lindex $filenames $idx}]

    foreach item $filenames {
        set path [file split  [file normalize $item]]
        set lib [::struct::set intersect $libs $path]
        puts $path
        if { [file extension $item] == ".vhd" } {
            read_vhdl -library $lib $item
        }
        if { [file extension $item] == ".v" } {
            read_verilog -library $lib $item
        }
        if { [file extension $item] == ".sv" } {
            read_verilog -sv -library $lib $item
        }
    }
}