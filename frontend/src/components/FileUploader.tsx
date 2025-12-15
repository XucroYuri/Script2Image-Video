import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { UploadCloud, FileJson } from 'lucide-react';

interface FileUploaderProps {
    onUpload: (file: File) => void;
    isLoading?: boolean;
}

const FileUploader: React.FC<FileUploaderProps> = ({ onUpload, isLoading }) => {
    const onDrop = useCallback((acceptedFiles: File[]) => {
        if (acceptedFiles.length > 0) {
            onUpload(acceptedFiles[0]);
        }
    }, [onUpload]);

    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop,
        accept: {
            'application/json': ['.json']
        },
        maxFiles: 1,
        disabled: isLoading
    });

    return (
        <div 
            {...getRootProps()} 
            className={`
                border-2 border-dashed rounded-xl p-10 text-center cursor-pointer transition-all
                ${isDragActive ? 'border-blue-500 bg-blue-50/10' : 'border-gray-600 hover:border-blue-400 hover:bg-gray-800/50'}
                ${isLoading ? 'opacity-50 cursor-not-allowed' : ''}
            `}
        >
            <input {...getInputProps()} />
            <div className="flex flex-col items-center justify-center gap-4">
                <div className="p-4 bg-gray-800 rounded-full">
                    {isLoading ? (
                        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
                    ) : (
                        <UploadCloud className="w-8 h-8 text-blue-400" />
                    )}
                </div>
                <div>
                    <h3 className="text-lg font-semibold text-white">
                        {isDragActive ? "Drop the JSON file here" : "Upload Project JSON"}
                    </h3>
                    <p className="text-gray-400 mt-1 text-sm">
                        Drag & drop or click to select
                    </p>
                </div>
                {!isLoading && (
                    <div className="flex items-center gap-2 text-xs text-gray-500 bg-gray-800 px-3 py-1 rounded-full">
                        <FileJson className="w-3 h-3" />
                        <span>Only .json files supported</span>
                    </div>
                )}
            </div>
        </div>
    );
};

export default FileUploader;
