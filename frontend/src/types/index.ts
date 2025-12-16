export interface NanoBananaPrompts {
    start: string;
    middle: string;
    end: string;
}

export interface Shot {
    shot_id: string;
    scene_id: string;
    name?: string;
    description?: string;
    order_index: number;
    nano_banana_pro_prompts?: NanoBananaPrompts;
    veo_3_1_prompt?: string;
}

export interface Scene {
    scene_id: string;
    project_id?: string;
    scene_title?: string;
    timestamp?: string;
    shots: Shot[];
}

export interface ProjectData {
    project: string;
    core_style?: Record<string, any>;
    character_references?: Record<string, string>;
    scenes: Scene[];
}

export interface GeneratedFile {
    file_id: string;
    shot_id: string;
    file_type: 'image' | 'video';
    file_path: string;
    file_url?: string;
    file_name: string;
    created_at: string;
    file_size: number;
}

export type GenerationStatus = 'idle' | 'pending' | 'generating' | 'completed' | 'failed';

export interface TaskState {
    id: string;
    status: GenerationStatus;
    type: 'image' | 'video';
    progress?: number;
    error?: string;
    result?: GeneratedFile;
}
