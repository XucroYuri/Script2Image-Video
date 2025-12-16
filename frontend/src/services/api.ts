import axios from 'axios';
import { ProjectData, GeneratedFile } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const uploadJson = async (file: File): Promise<ProjectData> => {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await api.post<ProjectData>('/upload-json', formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
    return response.data;
};

export const generateImage = async (params: {
    project_name: string;
    scene_id: string;
    shot_id: string;
    prompt: string;
    frame_type: string;
}): Promise<GeneratedFile> => {
    const response = await api.post<GeneratedFile>('/generate-image', params);
    return response.data;
};

export const generateVideo = async (params: {
    project_name: string;
    scene_id: string;
    shot_id: string;
    prompt: string;
}): Promise<GeneratedFile> => {
    const response = await api.post<GeneratedFile>('/generate-video', params);
    return response.data;
};

export default api;
