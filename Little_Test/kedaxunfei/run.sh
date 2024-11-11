# inpfile=../MCP/11_anli/plain_text/train_r1-00000-of-00001.parquet
# outfile=./json/11_anli.train_r1-00000-of-00001.json
# python -m pdb preprocess.py $inpfile $outfile

root_dir=../MCP
for task in $(ls $root_dir)
do
    if [ -d "$root_dir/$task" ]; then
        for sub_dir in $(ls $root_dir/$task)
        do
            if [ -d "$root_dir/$task/$sub_dir" ]; then
                for f in $(ls $root_dir/$task/$sub_dir)
                do
                    if [ -f "$root_dir/$task/$sub_dir/$f" ]; then
                        filename=$(basename "$root_dir/$task/$sub_dir/$f")
                        filename_without_extension=${filename%.*}
                        inpfile=$root_dir/$task/$sub_dir/$f
                        outfile=./json/$task.$filename_without_extension.json
                        python preprocess.py $inpfile $outfile
                    fi
                done
            fi
        done
    fi
done